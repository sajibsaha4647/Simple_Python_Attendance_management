"""Pure business rules for employees. No Django, no database."""
from dataclasses import replace

from apps.employee.domain.exceptions import EmployeeError


def normalize_name(name: str) -> str:
    """Trim the name and collapse repeated spaces: '  John   Doe ' -> 'John Doe'."""
    return " ".join(name.split())


def normalize_email(email: str) -> str:
    """Emails are compared case-insensitively, so store them trimmed and lowercase."""
    return email.strip().lower()


def clean_employee(data):
    """Normalize and validate employee data (any dataclass with name, email, salary).

    Returns a cleaned copy, or raises EmployeeError if a rule is broken.
    """
    data = replace(
        data,
        name=normalize_name(data.name),
        email=normalize_email(data.email),
    )

    if not data.name:
        raise EmployeeError("Employee name is required")
    if not data.email:
        raise EmployeeError("Email is required")
    if data.salary < 0:
        raise EmployeeError("Salary cannot be negative")

    return data
