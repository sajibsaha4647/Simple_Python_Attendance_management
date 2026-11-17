# Django discovers models here; the real ones live in the domain layer.
from .domain.models import *  # noqa: F401,F403
