from django.db import IntegrityError

from apps.employee.application.dto import CreateEmployeeDTO, EmployeeDTO
from apps.employee.application.interfaces import EmployeeRepository
from apps.employee.domain.exceptions import EmployeeError
from apps.employee.infrastructure.models import EmployeeModel


class DjangoEmployeeRepository(EmployeeRepository):
    def create(self, data: CreateEmployeeDTO) -> EmployeeDTO:
        try:
            row = EmployeeModel.objects.create(
                name=data.name,
                email=data.email,
                phone=data.phone,
                salary=data.salary,
            )
        except IntegrityError:
            raise EmployeeError(
                f"An employee with email {data.email} already exists")
        return self._to_dto(row)

    @staticmethod
    def _to_dto(row: EmployeeModel) -> EmployeeDTO:
        return EmployeeDTO(
            id=row.id,
            name=row.name,
            email=row.email,
            phone=row.phone,
            salary=row.salary,
            is_active=row.is_active,
        )
