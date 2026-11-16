from abc import ABC, abstractmethod

from apps.employee.application.dto import CreateEmployeeDTO, EmployeeDTO


class EmployeeRepository(ABC):
    @abstractmethod
    def create(self, data: CreateEmployeeDTO) -> EmployeeDTO:
        """Persist a new employee and return it with its id set."""
