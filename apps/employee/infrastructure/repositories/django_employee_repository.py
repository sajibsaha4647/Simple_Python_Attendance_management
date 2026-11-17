from apps.employee.application.dto import CreateEmployeeDTO, EmployeeDTO , UpdateEmployeeDTO
from apps.employee.application.interfaces import EmployeeRepository
from apps.employee.domain.models import EmployeeModel


class DjangoEmployeeRepository(EmployeeRepository):
    def create(self, data: CreateEmployeeDTO) -> EmployeeDTO | None:
        try:
            row = EmployeeModel.objects.create(
                name=data.name,
                email=data.email,
                phone=data.phone,
                salary=data.salary,
            )
        except Exception as error:
            print(f"Create employee failed: {error}")
            return None
        return self._to_dto(row)

    def get_by_id(self, empid)->EmployeeDTO|None:
        row =  EmployeeModel.objects.filter(id=empid).first()
        return self._to_dto(row) if row else None

    def get_all(self)->list[EmployeeDTO]:
        employees = EmployeeModel.objects.all()
        employees = employees.order_by("-id")
        employee_dtos = []

        for employee in employees:
            employee_dtos = self._to_dto(employee)
            employee_dtos.append(employee_dtos)


        return employee_dtos

    def update(self, data:UpdateEmployeeDTO)-> EmployeeDTO | None:
        row= EmployeeModel.objects.filter(id=data.id).first()
        if row is None:
            return None
        row.name = data.name
        row.email = data.email
        row.phone = data.phone
        row.salary = data.salary
        row.save()
        return self._to_dto(row)

    def delete(self, empid:int)->None:
        EmployeeModel.objects.filter(id=empid).delete()
    



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
