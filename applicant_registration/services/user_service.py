import secrets
import string
from django.db import transaction
from ..models import User, Application
from ..enums import UserRole, StatusApplication
from .notification_service import send_notification
from .send_credentials import send_credentials

def generate_pwd(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

def create_pre_registration(data):
    with transaction.atomic():

        try: 
            if User.objects.filter(email = data['email']).exists():
                raise ValueError("Correo electrónico ya esta registrado")
            
            random_pwd = generate_pwd()

            user = User.objects.create_user(
                document_type = data['document_type'],
                document_number = data['document_number'],
                name = data['name'],
                last_name = data['last_name'],
                gender = data['gender'],
                phone = data['phone'],
                email = data['email'],
                password = random_pwd,
                role = UserRole.ASP,
            )

            application = Application.objects.create(
                user = user,
                program = data['program'],
                applicant_type = data['applicant_type'],
                status = StatusApplication.PREI
            )

            send_credentials(user, random_pwd)
            send_notification(application)
        
        except Exception as e:
            return {
                "msg_error": str(e)
            }

    return {
        "user": user,
        "application": application
    }