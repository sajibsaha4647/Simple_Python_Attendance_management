from abc import ABC, abstractmethod

from apps.employee.application.dto import CreateEmployeeDTO, EmployeeDTO , UpdateEmployeeDTO


class EmployeeRepository(ABC):
    @abstractmethod
    def create(self, data: CreateEmployeeDTO) -> EmployeeDTO:
        """Persist a new employee and return it with its id set."""

    @abstractmethod
    def get_by_id(self, empid:int)->CreateEmployeeDTO | None:
        ...

    @abstractmethod
    def get_all(self)->list[EmployeeDTO]:
        ...
    
    @abstractmethod
    def update(self,data:UpdateEmployeeDTO)-> EmployeeDTO: ...
    
    @abstractmethod
    def delete(self,empid:int)->None:
        ...