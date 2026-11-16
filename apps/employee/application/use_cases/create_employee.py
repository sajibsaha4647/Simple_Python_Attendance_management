from apps.employee.application.dto import CreateEmployeeDTO
from apps.employee.application.interfaces import EmployeeRepository
from apps.employee.domain.entities import Employee


class CreateEmployee:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def execute(self, data: CreateEmployeeDTO) -> Employee:
        # The entity validates itself (name, email, salary) on creation.
        employee = Employee(
            name=data.name,
            email=data.email,
            phone=data.phone,
            salary=data.salary,
        )
        return self.repository.create(employee)
