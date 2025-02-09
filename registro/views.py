from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Especialidad
from .forms import PacienteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db import models
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string

User = get_user_model()

class CustomLoginView(LoginView):
    template_name = 'registro/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.is_admin:
            return redirect('admin:index')
        else:
            return redirect('registrar_paciente')
        
        
        
        
from django.db.models import Count, Avg

@login_required
def index(request):
    especialidad_usuario = request.user.especialidad.nombre
    total_pacientes = Paciente.objects.count()
    promedio_edad = Paciente.objects.aggregate(Avg('edad'))['edad__avg']
    distribucion_especialidades = Paciente.objects.values('especialidad__nombre').annotate(total=Count('id'))
    distribucion_sexo = Paciente.objects.values('sexo').annotate(total=Count('id'))
    promedio_imc = Paciente.objects.aggregate(Avg('imc'))['imc__avg']
    
    # Procesar la distribución de IMC
    imc_labels = ["Delgadez severa", "Delgadez moderada", "Delgadez leve", "Peso normal", "Sobrepeso", "Obesidad grado I", "Obesidad grado II", "Obesidad grado III (obesidad mórbida)"]
    distribucion_imc = {label: 0 for label in imc_labels}
    for item in Paciente.objects.values('diagnostico_imc').annotate(total=Count('id')):
        if item['diagnostico_imc'] in distribucion_imc:
            distribucion_imc[item['diagnostico_imc']] = item['total']
    
    distribucion_imc_list = [distribucion_imc[label] for label in imc_labels]
    
    top_sectores = Paciente.objects.values('sector').annotate(total=Count('id')).order_by('-total')[:5]

    context = {
        'especialidad_usuario': especialidad_usuario,
        'total_pacientes': total_pacientes,
        'promedio_edad': promedio_edad,
        'distribucion_especialidades': distribucion_especialidades,
        'distribucion_sexo': distribucion_sexo,
        'promedio_imc': promedio_imc,
        'distribucion_imc': distribucion_imc_list,
        'top_sectores': top_sectores,
    }
    return render(request, 'registro/index.html', context)



@login_required
def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.edad = calcular_edad(form.cleaned_data['fecha_nacimiento'])
            paciente.imc = calcular_imc(form.cleaned_data['peso'], form.cleaned_data['talla'])
            paciente.diagnostico_imc = diagnosticar_imc(paciente.imc)
            paciente.especialidad = request.user.especialidad
            paciente.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    return render(request, 'registro/registrar_paciente.html', {'form': form})

@login_required
def buscar_paciente(request):
    query = request.GET.get('query', '')
    especialidad = request.user.especialidad
    resultados = Paciente.objects.filter(especialidad=especialidad).filter(
        models.Q(cedula__icontains=query) | models.Q(apellidos_nombres__icontains=query)
    )
    return render(request, 'registro/buscar_paciente.html', {'resultados': resultados})

@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, especialidad=request.user.especialidad)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.edad = calcular_edad(form.cleaned_data['fecha_nacimiento'])
            paciente.imc = calcular_imc(form.cleaned_data['peso'], form.cleaned_data['talla'])
            paciente.diagnostico_imc = diagnosticar_imc(paciente.imc)
            paciente.save()
            return redirect('buscar_paciente')
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'registro/editar_paciente.html', {'form': form})


@login_required
def visualizar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id, especialidad=request.user.especialidad)
    return render(request, 'registro/visualizar_paciente.html', {'paciente': paciente})


@login_required
def descargar_pdf(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)

    # Renderizar el HTML
    html_string = render_to_string('registro/paciente_pdf.html', {'paciente': paciente})

    # Generar PDF
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    # Crear la respuesta HTTP con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Paciente_{paciente.cedula}.pdf"'
    
    return response

import weasyprint
@login_required
def descargar_paciente_pdf(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    html_string = render_to_string('registro/paciente_pdf.html', {'paciente': paciente})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=paciente_{paciente.cedula}.pdf'
    weasyprint.HTML(string=html_string).write_pdf(response)
    return response

def calcular_edad(fecha_nacimiento):
    from datetime import date
    hoy = date.today()
    return hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

def calcular_imc(peso, talla):
    return round(float(peso) / (float(talla) ** 2), 2)

def diagnosticar_imc(imc, edad=None):
    if isinstance(edad, str) and 'meses' in edad:
        return 'Diagnóstico pediátrico no implementado'

    if imc < 16:
        return 'Delgadez severa'
    elif 16 <= imc < 17:
        return 'Delgadez moderada'
    elif 17 <= imc < 18.5:
        return 'Delgadez leve'
    elif 18.5 <= imc < 25:
        return 'Peso normal'
    elif 25 <= imc < 30:
        return 'Sobrepeso'
    elif 30 <= imc < 35:
        return 'Obesidad grado I'
    elif 35 <= imc < 40:
        return 'Obesidad grado II'
    else:
        return 'Obesidad grado III (obesidad mórbida)'