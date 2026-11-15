from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import EmployeeForm


def create_employee(request):
    form = EmployeeForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        employee = form.save()
        messages.success(request, f'Employee "{employee.name}" created.')
        return redirect('employee:create')

    return render(request, 'employee/create.html', {'form': form})
