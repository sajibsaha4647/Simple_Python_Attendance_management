from decimal import Decimal

from django.contrib import messages
from django.shortcuts import redirect, render

from apps.employee.application.dto import CreateEmployeeDTO
from apps.employee.domain.services import clean_employee
from apps.employee.infrastructure.repositories import DjangoEmployeeRepository


def create_employee(request):
    errors = []
    values = {}

    if request.method == 'POST':
        values = {key: request.POST.get(key, '').strip()
                  for key in ('name', 'email', 'phone', 'salary')}

        try:
            salary = Decimal(values['salary'])
        except Exception as error:
            print(f"Salary error: {error!r}")
            errors.append("Salary must be a number")
        else:
            try:
                data = clean_employee(CreateEmployeeDTO(
                    name=values['name'],
                    email=values['email'],
                    phone=values['phone'],
                    salary=salary,
                ))
                employee = DjangoEmployeeRepository().create(data)
            except Exception as error:
                print(f"Create employee error: {error!r}")
                errors.append(str(error))
            else:
                if employee is None:
                    errors.append("Could not save the employee. Check the server console.")
                else:
                    messages.success(request, f'Employee "{employee.name}" created.')
                    return redirect('employee:create')

    return render(request, 'employee/create.html', {'errors': errors, 'values': values})
