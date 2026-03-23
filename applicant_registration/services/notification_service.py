from django.core.mail import send_mail
from ..models import Notification
from ..enums import StatusApplication, UserRole
from ..helpers import emails_helpers

def send_notification(applicant, observation=None):
    subject = None
    message = None
    recipients = []
    user = applicant.user

    match applicant.status:
        case StatusApplication.PREI:
            subject = "Nueva Pre-Inscripcion" 
            message = "Se ha registrado una nueva pre-inscripción"
            recipients = emails_helpers.get_emails_by_roles([
                UserRole.RYC,
                UserRole.CPG,
                UserRole.MEI
            ])

        case StatusApplication.FINA:
            subject = "Inscripción finalizada"
            message = "El registro ha finalizado completamente para validación"
            recipients = emails_helpers.get_emails_by_roles([
                UserRole.RYC
            ])
        
        case StatusApplication.CORR:
            subject = "Correción/Observación inscripción"
            message = "La solicitud no ha sido aprobada, verificar la información"
            recipients = emails_helpers.get_emails_by_roles([
                UserRole.RYC,
                UserRole.MEI
            ])
            if observation:
                message += f"Observación: {observation}"

        case StatusApplication.APRO:
            subject = "Inscripción aprobada"
            message = "La solicitud ha sido aprobada exitosamente!"
            recipients = emails_helpers.get_emails_by_roles([
                UserRole.CPG,
                UserRole.ASP
            ])

        case StatusApplication.REJE:
            subject = "Inscripción rechazada"
            message = "La solicitud fue rechazada"
            if observation:
                message += f"Observación: {observation}"
            recipients = [user.email]
        
        case StatusApplication.ADMI:
            subject = "Inscripción admitida"
            message = "Bienvenido!, tu solicitud ha sido admitida"
            recipients = [user.email]

        case _:
            return
        
    recipients = list(set(recipients))
    
    send_mail(
        subject,
        message,
        'no-replay@udes.test.co',
        recipients,
        fail_silently=False,
    )

    for email in recipients:
        Notification.objects.create(
            application=applicant,
            email_user=email,
            email_aspiring=user.email,
            observation=observation or ""
        )



