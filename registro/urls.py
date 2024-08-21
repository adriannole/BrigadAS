# urls.py

from django.urls import path, include
from .views import CustomLoginView, index, registrar_paciente, buscar_paciente, editar_paciente, visualizar_paciente, descargar_pdf
from django.contrib import admin
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .views import descargar_paciente_pdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Define la ruta para index
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('registrar/', registrar_paciente, name='registrar_paciente'),
    path('buscar/', buscar_paciente, name='buscar_paciente'),
    path('editar/<int:paciente_id>/', editar_paciente, name='editar_paciente'),
    path('visualizar/<int:paciente_id>/', visualizar_paciente, name='visualizar_paciente'),
    path('descargar_pdf/<int:paciente_id>/', descargar_pdf, name='descargar_pdf'),
    path('descargar_paciente_pdf/<int:paciente_id>/', descargar_paciente_pdf, name='descargar_paciente_pdf'),

]