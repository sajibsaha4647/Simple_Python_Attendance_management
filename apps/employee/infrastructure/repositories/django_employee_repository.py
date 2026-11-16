from django.db import IntegrityError

from apps.employee.application.interfaces import EmployeeRepository
from apps.employee.domain.entities import Employee
from apps.employee.domain.exceptions import EmployeeError
from apps.employee.infrastructure.models import EmployeeModel


class DjangoEmployeeRepository(EmployeeRepository):
    def create(self, employee: Employee) -> Employee:
        try:
            row = EmployeeModel.objects.create(
                name=employee.name,
                email=employee.email,
                phone=employee.phone,
                salary=employee.salary,
                is_active=employee.is_active,
            )
        except IntegrityError:
            raise EmployeeError(
                f"An employee with email {employee.email} already exists")
        return self._to_entity(row)

    @staticmethod
    def _to_entity(row: EmployeeModel) -> Employee:
        return Employee(
            id=row.id,
            name=row.name,
            email=row.email,
            phone=row.phone,
            salary=row.salary,
            is_active=row.is_active,
        )
