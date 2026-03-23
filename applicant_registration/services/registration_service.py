from django.db import transaction
from ..models import Application, Registration
from ..enums import StatusApplication
from ..services.notification_service import send_notification

def create_complete_registration(application_id, data):
    with transaction.atomic():

        application = Application.objects.get(id=application_id)
        if hasattr(application, 'registration'):
            raise ValueError("La inscripcion fue totalmente diligenciada")
        registration = Registration.objects.create(
            date_birth = data['date_birth'],
            place_birth = data['place_birth'],
            home_address = data['home_address'],
            stratum = data['stratum'],
            photo=data.get('photo'),
            document=data.get('document'),
            diploma=data.get('diploma'),
            question_one=data['question_one'],
            question_two=data['question_two'],
            question_three=data['question_three'],
            application=application
        )
        application.status = StatusApplication.FINA
        application.save()
        send_notification(application)
    
    return registration