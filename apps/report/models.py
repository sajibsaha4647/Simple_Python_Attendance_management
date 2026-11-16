# Django discovers models here; the real ones live in the infrastructure layer.
from .infrastructure.models import *  # noqa: F401,F403
