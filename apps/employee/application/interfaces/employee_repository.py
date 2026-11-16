from abc import ABC, abstractmethod

from apps.employee.domain.entities import Employee


class EmployeeRepository(ABC):
    @abstractmethod
    def create(self, employee: Employee) -> Employee:
        """Persist a new employee and return it with its id set."""
