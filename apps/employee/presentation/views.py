from django.contrib import messages
from django.shortcuts import redirect, render

from apps.employee.application.dto import CreateEmployeeDTO
from apps.employee.application.use_cases import CreateEmployee
from apps.employee.domain.exceptions import EmployeeError
from apps.employee.infrastructure.repositories import DjangoEmployeeRepository

from .forms import EmployeeForm


def create_employee(request):
    form = EmployeeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        use_case = CreateEmployee(DjangoEmployeeRepository())
        try:
            employee = use_case.execute(CreateEmployeeDTO(**form.cleaned_data))
        except EmployeeError as error:
            form.add_error(None, str(error))
        else:
            messages.success(request, f'Employee "{employee.name}" created.')
            return redirect('employee:create')

    return render(request, 'employee/create.html', {'form': form})
