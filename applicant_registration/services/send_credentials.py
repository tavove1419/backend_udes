from django.core.mail import send_mail

def send_credentials(user, random_pwd):
    subject = "Informació de acceso - UDES"
    message = f"""Saludos, {user.name}.
                
                El proceso de pre-inscripción ha sido exitosa.

                Para continuar con el proceso de inscripción, 
                ingresa al sistema con las siguientes credenciales:

                Correo: {user.email}
                Password: {random_pwd}

                Link para ingresar: http://localhost:9000/login
            """
    send_mail(
        subject,
        message,
        None,
        [user.email],
        fail_silently=False
    )
