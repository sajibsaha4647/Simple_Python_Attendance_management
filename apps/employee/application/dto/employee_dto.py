from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateEmployeeDTO:
    name: str
    email: str
    phone: str
    salary: Decimal
