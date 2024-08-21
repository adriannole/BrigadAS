# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class User(AbstractUser):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.SET_NULL, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    # Relaciona correctamente los permisos y grupos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='registro_user_set',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='registro_user_permissions_set',
        blank=True,
    )



class Paciente(models.Model):
    SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ]
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10)
    apellidos_nombres = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    sector = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()
    afiliado_seguro = models.BooleanField(default=False)
    discapacidad = models.BooleanField(default=False)
    porcentaje_discapacidad = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tipo_discapacidad = models.CharField(max_length=100, null=True, blank=True)
    antecedentes_patologicos_personales = models.TextField()
    antecedentes_patologicos_familiares = models.TextField()
    presion_arterial = models.CharField(max_length=20, null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    talla = models.DecimalField(max_digits=5, decimal_places=2)
    imc = models.DecimalField(max_digits=5, decimal_places=2)
    diagnostico_imc = models.CharField(max_length=100)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1)
    frecuencia_cardiaca = models.IntegerField()
    frecuencia_respiratoria = models.IntegerField()
    nivel_glucosa = models.DecimalField(max_digits=5, decimal_places=2)
    saturacion = models.DecimalField(max_digits=5, decimal_places=2)
    diagnostico = models.TextField()
    cie_10 = models.CharField(max_length=20, default="No especificado")
    observacion = models.TextField()
    responsable = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.apellidos_nombres} - {self.cedula}'
