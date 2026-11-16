from dataclasses import dataclass
from decimal import Decimal


@dataclass
class CreateEmployeeDTO:
    """Request model: what comes in from the client."""
    name: str
    email: str
    phone: str
    salary: Decimal


@dataclass
class EmployeeDTO:
    """Response model: what goes back out after saving."""
    id: int
    name: str
    email: str
    phone: str
    salary: Decimal
    is_active: bool
