from dataclasses import dataclass
from decimal import Decimal

from apps.employee.domain.exceptions import EmployeeError
from apps.employee.domain.services import normalize_email, normalize_name


@dataclass
class Employee:
    name: str
    email: str
    phone: str
    salary: Decimal
    is_active: bool = True
    id: int | None = None

    def __post_init__(self):
        self.name = normalize_name(self.name)
        self.email = normalize_email(self.email)

        if not self.name:
            raise EmployeeError("Employee name is required")
        if not self.email:
            raise EmployeeError("Email is required")
        if self.salary < 0:
            raise EmployeeError("Salary cannot be negative")
