from django.db import transaction
from ..models import Application, Session
from ..enums import StatusApplication

def create_session(user):
    with transaction.atomic():
        session_first = not Session.objects.filter(user=user).exists()
        Session.objects.filter(user=user, is_active=True).update(is_active=False)
        session = Session.objects.create(user=user, is_active = True)
        application = Application.objects.filter(
            user=user,
            status=StatusApplication.PREI
        ).first()

        if session_first and application:
            application.status = StatusApplication.FORM
            application.save()
    return session