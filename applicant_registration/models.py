import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .enums import UserRole, StatusApplication

#Usuario
class UserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("El correo electrónico es obligatorio")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

#Usuario 
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document_type = models.CharField(max_length=20)
    document_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=3,
        choices=UserRole.choices
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"

#Inscripcion - Solicitud
class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    program = models.CharField(max_length=100)
    applicant_type = models.CharField(max_length=50)
    status = models.CharField(
        max_length=4,
        choices=StatusApplication.choices,
        default=StatusApplication.PREI
    )
    observation = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# Registro de inscripcion.
class Registration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_birth = models.DateField(
        verbose_name="Fecha de nacimiento",
        null=False,
    )
    place_birth = models.CharField(
        verbose_name= "Lugar de nacimiento",
        max_length=100,
        null=False
    )
    home_address = models.CharField(verbose_name="Direccion residencia",max_length=150)
    stratum = models.PositiveSmallIntegerField(
        verbose_name="Estrato"
    )
    photo = models.ImageField(upload_to='photos/')
    document = models.FileField(upload_to='documents/')
    diploma = models.FileField(upload_to='diplomas/')
    question_one = models.TextField()
    question_two = models.CharField(verbose_name="Pregunta dos",max_length=100)
    question_three = models.CharField(verbose_name="Pregunta tres",max_length=100)
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Bitacora de inicio de sesiones.
class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sesion_date = models.DateTimeField(
        verbose_name="Fecha de sesion",
        auto_now_add=True
    )
    is_active = models.BooleanField(
        verbose_name="Estado sesion",
        default=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

# Notificaciones.
class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
    )
    email_user = models.EmailField(
        verbose_name="Email de usuario a validar",
    )
    email_aspiring = models.EmailField(
        verbose_name="Email del aspirante",
    )
    send_date = models.DateTimeField(auto_now_add=True)
    observation = models.TextField(verbose_name="Observaciones")
    created_at = models.DateTimeField(auto_now_add=True)

