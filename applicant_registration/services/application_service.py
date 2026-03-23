from django.db import transaction
from ..enums import StatusApplication
from .notification_service import send_notification
from ..models import User, Application, Registration
from django.shortcuts import get_object_or_404
import json

#Aprobar la inscripcion

def approved(application, user, observation=None):

    if user.role != 'RYC':
        raise ValueError("Usuario no autorizado")
    
    if application.status == StatusApplication.ADMI or application.status == StatusApplication.REJE:
        raise ValueError("Solicitud cerrada por aprobación o rechazo")

    with transaction.atomic():
        application.status = StatusApplication.APRO
        application.observation = observation
        application.save()

        send_notification(application, observation)
    return application


#Devolver la inscripcion para corregir u observaciones

def correction(application, user, observation=None):
    
    if user.role != 'RYC':
        raise ValueError("Usuario no autorizado")
    
    with transaction.atomic():
        application.status = StatusApplication.CORR
        application.observation = observation
        application.save()

        send_notification(application, observation)
    
    return application


#Admitir o rechazar la solicitud

def accept_reject(application, user, status, observation=None):

    if user.role != 'CPG':
        raise ValueError("Usuario no autorizado")
    
    if application.status != StatusApplication.APRO:
        raise ValueError("La solicitud deber estar aprobada")

    if status not in [StatusApplication.ADMI, StatusApplication.REJE]:
        raise ValueError("El estado es inválido")
    
    with transaction.atomic():
        application.status = status
        application.observation = observation
        application.save()

        send_notification(application, observation)
    
    return application

#Actualizar correciones u observaciones de la solicitud

def update_applicant(applicant, user, data):
    
    if user.role != 'MEI':
        raise ValueError("Usuario no autorizado")
    
    if applicant.status != StatusApplication.CORR:
        raise ValueError("No es posible actualizarse la solicutud en este estado(status)")

    with transaction.atomic():
        
        try:
            user_data = json.loads(data.data.get('user', '{}'))
            application_data = json.loads(data.data.get('application', '{}'))
            registration_data = json.loads(data.data.get('registration', '{}'))
        except json.JSONDecodeError:
            raise ValueError("Error al parsear los datos JSON")
        
        user_obj = applicant.user

        for field, value in user_data.items():
            if hasattr(user_obj, field):
                setattr(user_obj, field, value)

        user_obj.save()

        for field, value in application_data.items():
            if hasattr(applicant, field):
                setattr(applicant, field, value)

        applicant.save()

        try:
            registration = applicant.registration
        except Registration.DoesNotExist:
            raise ValueError("Registro no existe")

        for field, value in registration_data.items():
            if hasattr(registration, field):
                setattr(registration, field, value)

        files = data.FILES if hasattr(data, 'FILES') else {}

        if 'photo' in files:
            registration.photo = files['photo']

        if 'document' in files:
            registration.document = files['document']

        if 'diploma' in files:
            registration.diploma = files['diploma']

        registration.save()

        applicant.status = StatusApplication.FINA
        applicant.save()
    
    return applicant

def list_applications(filters=None):
    queryset = Application.objects.select_related('user').all()

    if filters:
        user_id = filters.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
    
    return queryset


def get_application_full(application_id):
    application = get_object_or_404(
        Application.objects.select_related('user', 'registration'),
        id=application_id
    )
    return application