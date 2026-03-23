from django.db import models

class UserRole(models.TextChoices):
    ASP = 'ASP', 'Aspirante',
    RYC = 'RYC', 'Registro y Control',
    MEI = 'MEI', 'Mercadeo Institucional',
    CPG = 'CPG', 'Coordinador de Programa'

class StatusApplication(models.TextChoices):
    PREI = 'PREI', 'Pre-inscripción'
    FORM = 'FORM', 'Diligenciando formulario'
    FINA = 'FINA', 'Finalizo inscripción formulario completo'
    APRO = 'APRO', 'Aprobada la inscripción'
    CORR = 'CORR', 'Corregir la inscripción'
    ADMI = 'ADMI', 'Admitido'
    REJE = 'REJE', 'Rechazado'
