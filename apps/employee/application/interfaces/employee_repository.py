from abc import ABC, abstractmethod 

from apps.employee.domain.entities.employee import Employee

class EmployeeRepository:


    @abstractmethod
    def create_employee(self,Employee)->Employee:
        pass

    @abstractmethod
    def get_ById_employee(self,employee_id:int)->Employee | None :
        pass

    @abstractmethod
    def get_all_employee(self)->list[Employee]:
        pass

    @abstractmethod
    def update(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def delete(self, employee_id: int) -> None:
        pass