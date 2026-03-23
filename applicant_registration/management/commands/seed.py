from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from applicant_registration.enums import UserRole

User = get_user_model()

class Command(BaseCommand):

    help = 'Seed creacion inicial de usuarios'

    def handle(self, *args, **options):

        self.stdout.write("Seed Iniciando creación de usuarios")
        
        #Creación de usuario de registro y control
        if not User.objects.filter(email="gustavo.vega@gmail.com").exists():
            User.objects.create_superuser(
                document_type="CC",
                document_number="12345",
                name="User RYC",
                last_name="Registro y control",
                gender="M",
                phone="300000000",
                email="gustavo.vega@gmail.com",
                password="Ryc1234*",
                role=UserRole.RYC,
                is_staff=False
            )
            self.stdout.write(self.style.SUCCESS("Usuario RYC registrado correctamente!"))
        else:
            self.stdout.write("Usuario RYC ya existe")
        
        # Creación de usuario mercadeo institucional
        if not User.objects.filter(email="contactonimet@gmail.com").exists():
            User.objects.create_superuser(
                document_type="CC",
                document_number="54321",
                name="User MEI",
                last_name="Mercadeo institucional",
                gender="M",
                phone="300000000",
                email="contactonimet@gmail.com",
                password="Mei1234*",
                role=UserRole.MEI,
                is_staff=False
            )
            self.stdout.write(self.style.SUCCESS("Usuario MEI registrado correctamente!"))
        else:
            self.stdout.write("Usuario MEI ya existe")
        
        #Creación de usuario de Coordinador de programa
        if not User.objects.filter(email="magentos08@gmail.com").exists():
            User.objects.create_superuser(
                document_type="CC",
                document_number="98765",
                name="User CPG",
                last_name="Coordinador de programa",
                gender="M",
                phone="300000000",
                email="magentos08@gmail.com",
                password="Cpg1234*",
                role=UserRole.CPG,
                is_staff=False
            )
            self.stdout.write(self.style.SUCCESS("Usuario CPG registrado correctamente!"))
        else:
            self.stdout.write("Usuario CPG ya existe")
        
        self.stdout.write(self.style.SUCCESS("Seed finalizado"))
