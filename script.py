from django.contrib.auth import get_user_model
from registro.models import Especialidad

User = get_user_model()

# Verifica si la especialidad ya existe, si no, la crea
especialidad, created = Especialidad.objects.get_or_create(nombre='MEDICINA GENERAL')

# Crea el usuario
username = 'nuevo_usuario'
password = 'contraseña_segura'
email = 'nuevo_usuario@example.com'

user = User.objects.create_user(username=username, password=password, email=email, especialidad=especialidad)
user.is_admin = False
user.save()

print(f'Usuario {username} creado con éxito.')