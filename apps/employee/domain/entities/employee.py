from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Employee:
    name:str
    email:str
    phone:str
    salary:Decimal
    is_active:bool = True
    id:int | None = None

    def __post_init__(self):
        if not self.name.strip:
            raise ValueError("Employee name is required")
        if not self.email.strip:
            raise ValueError("Email is required")
        if self.salary < 0:
            raise ValueError("Salary cannot be negative")