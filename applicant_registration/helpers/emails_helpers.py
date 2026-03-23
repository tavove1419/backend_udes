from ..models import User
from ..enums import UserRole

def get_emails_by_roles(role):
    return list(
        User
        .objects.filter(role__in=role)
        .values_list('email', flat=True)
    )