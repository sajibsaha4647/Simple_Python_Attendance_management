"""Pure business rules for employees. No Django, no database."""


def normalize_name(name: str) -> str:
    """Trim the name and collapse repeated spaces: '  John   Doe ' -> 'John Doe'."""
    return " ".join(name.split())


def normalize_email(email: str) -> str:
    """Emails are compared case-insensitively, so store them trimmed and lowercase."""
    return email.strip().lower()
