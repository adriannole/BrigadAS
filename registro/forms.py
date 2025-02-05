from django import forms
from .models import Paciente, Especialidad, User
from django.core.exceptions import ValidationError



####################################################################
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'especialidad', 'is_admin')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'especialidad', 'is_admin')






#####################################################







SECTORES = [
    ("HUERTOS FAMILIARES MEDICOS DE PICHINCHA", "HUERTOS FAMILIARES MEDICOS DE PICHINCHA"),
    ("PRADOS DEL VALLE - MIRANDA", "PRADOS DEL VALLE - MIRANDA"),
    ("ALAMOS DE MIRANDA ALTO", "ALAMOS DE MIRANDA ALTO"),
    ("COMITÉ PRO MEJORAS TENA", "COMITÉ PRO MEJORAS TENA"),
    ("TENA", "TENA"),
    ("MIRANDA GRANDE", "MIRANDA GRANDE"),
    ("LOS PINOS DE MIRANDA", "LOS PINOS DE MIRANDA"),
    ("MIRANDA BAJO", "MIRANDA BAJO"),
    ("GNRAL ELOY ALFARO", "GNRAL ELOY ALFARO"),
    ("EL JARDIN DE SANTA ISABEL", "EL JARDIN DE SANTA ISABEL"),
    ("MIRADOR SUR - MIRANDA", "MIRADOR SUR - MIRANDA"),
    ("PEDREGAL DE MIRANDA", "PEDREGAL DE MIRANDA"),
    ("SANTA ISABEL DE LOS MILITARES", "SANTA ISABEL DE LOS MILITARES"),
    ("CHAUPITENA", "CHAUPITENA"),
    ("BUEN VIVIR DE SANTA ISABEL", "BUEN VIVIR DE SANTA ISABEL"),
    ("SANTA ISABEL ANTIGUO", "SANTA ISABEL ANTIGUO"),
    ("COMITÉ PRO MEJORAS SANTA ISABEL", "COMITÉ PRO MEJORAS SANTA ISABEL"),
    ("HUERTOS FAMILIARES LAS FUENTES", "HUERTOS FAMILIARES LAS FUENTES"),
    ("LA PROVIDENCIA BAJA", "LA PROVIDENCIA BAJA"),
    ("LA PROVIDENCIA ALTA", "LA PROVIDENCIA ALTA"),
    ("SANTA ROSA DE CHILLO", "SANTA ROSA DE CHILLO"),
    ("SAN ANTONIO DE CHILLO", "SAN ANTONIO DE CHILLO"),
    ("LA BALVINA", "LA BALVINA"),
    ("MIRANDA GRANDE VISTA HERMOSA", "MIRANDA GRANDE VISTA HERMOSA"),
    ("PAULINA DEL HIERRO", "PAULINA DEL HIERRO"),
    ("SANTA ISABEL VISTA HERMOSA", "SANTA ISABEL VISTA HERMOSA"),
    ("CHILLO JIJON", "CHILLO JIJON"),
    ("SAN CARLOS", "SAN CARLOS"),
    ("LIBERTAD DE CATAGUANGO", "LIBERTAD DE CATAGUANGO"),
    ("CARAPUNGO ALTO", "CARAPUNGO ALTO"),
    ("CARAPUNGO BAJO", "CARAPUNGO BAJO"),
    ("HUERTO FAMILIARES CARAPUNGO", "HUERTO FAMILIARES CARAPUNGO"),
    ("SAN ANDRES", "SAN ANDRES"),
    ("SAN FERNANDO EL GALPON", "SAN FERNANDO EL GALPON"),
    ("YANAHUYCO", "YANAHUYCO"),
    ("SAN FERNANDO", "SAN FERNANDO"),
    ("LA FLORIDA", "LA FLORIDA"),
    ("NUEVOS HORIZONTES", "NUEVOS HORIZONTES"),
    ("LOTIZACION CARLOS", "LOTIZACION CARLOS"),
    ("LA PLAYITA DE AMAGUAÑA", "LA PLAYITA DE AMAGUAÑA"),
    ("LA VICTORIA", "LA VICTORIA"),
    ("JESUS DEL GRAN PODER - CUENDINA", "JESUS DEL GRAN PODER - CUENDINA"),
    ("SANTA TERESITA", "SANTA TERESITA"),
    ("UNIDAD BARRIAL CUENDINA", "UNIDAD BARRIAL CUENDINA"),
    ("SAN JUAN", "SAN JUAN"),
    ("CUENDINA CHICO", "CUENDINA CHICO"),
    ("SAN JUAN DE LA CRUZ", "SAN JUAN DE LA CRUZ"),
    ("SAN LUIS", "SAN LUIS"),
    ("GUAMBA", "GUAMBA"),
    ("LA UNION", "LA UNION"),
    ("EL ROSARIO", "EL ROSARIO"),
    ("LA VAQUERIA", "LA VAQUERIA"),
    ("COMUNA SANTA ROSA DE CUENDINA", "COMUNA SANTA ROSA DE CUENDINA"),
    ("RECINTO PASOCHOA", "RECINTO PASOCHOA"),
    ("SAN ANTONIO DE PASOCHOA", "SAN ANTONIO DE PASOCHOA"),
    ("PRO MEJORAS CUENDINA", "PRO MEJORAS CUENDINA"),
    ("LOS PINOS DE CUENDINA", "LOS PINOS DE CUENDINA"),
    ("MALINDA", "MALINDA"),
    ("GONZALEZ SUAREZ DE LA VICTORIA", "GONZALEZ SUAREZ DE LA VICTORIA"),
    ("SIMON BOLÍVAR DE LA VICTORIA", "SIMON BOLÍVAR DE LA VICTORIA"),
    ("LA CAROLINA", "LA CAROLINA"),
    ("COCHAPAMBA", "COCHAPAMBA"),
    ("SAN JOSE", "SAN JOSE"),
    ("CENTRO", "CENTRO"),
    ("SAN ROQUE", "SAN ROQUE"),
    ("PELUCHE BAJO", "PELUCHE BAJO"),
    ("PELUCHE ALTO", "PELUCHE ALTO"),
    ("BLANQUEDO", "BLANQUEDO"),
    ("COMUNA EL EJIDO", "COMUNA EL EJIDO"),
    ("SAN FRANCISCO", "SAN FRANCISCO"),
    ("PUCARA BAJO", "PUCARA BAJO"),
    ("PUCARA ALTO", "PUCARA ALTO"),
    ("SANTO DOMINGO DE AMAGUAÑA", "SANTO DOMINGO DE AMAGUAÑA"),
    ("EL RELICARIO", "EL RELICARIO")
]

BOOLEAN_CHOICES = [
    (True, 'Sí'),
    (False, 'No'),
]

SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
]

class PacienteForm(forms.ModelForm):
    especialidad = forms.ModelChoiceField(
        required=False, 
        queryset=Especialidad.objects.all(), 
        empty_label="Seleccione una especialidad", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    presion_arterial = forms.CharField(
        required=False,  # Aquí se hace que el campo no sea requerido
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sector = forms.ChoiceField(
        choices=SECTORES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sexo = forms.ChoiceField(
        choices=SEXO_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    afiliado_seguro = forms.ChoiceField(
        choices=BOOLEAN_CHOICES, 
        initial=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    discapacidad = forms.ChoiceField(
        choices=BOOLEAN_CHOICES, 
        initial=False,  # Aquí se establece el valor predeterminado en "No"
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    imc = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )
    diagnostico_imc = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )
    edad = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'})
    )

    class Meta:
        model = Paciente
        fields = [
            'cedula',
            'apellidos_nombres',
            'telefono',
            'sexo',
            'sector',
            'fecha_nacimiento',
            'edad',
            'afiliado_seguro',
            'discapacidad',
            'porcentaje_discapacidad',
            'tipo_discapacidad',
            'antecedentes_patologicos_personales',
            'antecedentes_patologicos_familiares',
            'presion_arterial',
            'peso',
            'talla',
            'imc',
            'diagnostico_imc',
            'temperatura',
            'frecuencia_cardiaca',
            'frecuencia_respiratoria',
            'nivel_glucosa',
            'saturacion',
            'diagnostico',
            'cie_10',
            'observacion',
            'responsable',
            'especialidad',
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control', 'type': 'date'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos_nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'porcentaje_discapacidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo_discapacidad': forms.TextInput(attrs={'class': 'form-control'}),
            'antecedentes_patologicos_personales': forms.Textarea(attrs={'class': 'form-control'}),
            'antecedentes_patologicos_familiares': forms.Textarea(attrs={'class': 'form-control'}),
            'presion_arterial': forms.TextInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_peso'}),
            'talla': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_talla'}),
            'temperatura': forms.NumberInput(attrs={'class': 'form-control'}),
            'frecuencia_cardiaca': forms.NumberInput(attrs={'class': 'form-control'}),
            'frecuencia_respiratoria': forms.NumberInput(attrs={'class': 'form-control'}),
            'nivel_glucosa': forms.NumberInput(attrs={'class': 'form-control'}),
            'saturacion': forms.NumberInput(attrs={'class': 'form-control'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control'}),
            'cie_10': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_cedula(self):
        cedula = self.cleaned_data.get('cedula')
        if len(cedula) != 10:
            raise ValidationError("La cédula debe tener exactamente 10 dígitos.")
        if not cedula.isdigit():
            raise ValidationError("La cédula debe contener solo números.")
        if Paciente.objects.filter(cedula=cedula).exists():
            raise ValidationError("Este usuario ya está registrado. Verifique en la base de datos.")
        return cedula


    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():
            raise ValidationError("El teléfono debe contener solo números.")
        if len(telefono) < 7 or len(telefono) > 10:
            raise ValidationError("El teléfono debe tener entre 7 y 10 dígitos.")
        return telefono

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso <= 0:
            raise ValidationError("El peso debe ser un valor positivo.")
        return peso

    def clean_talla(self):
        talla = self.cleaned_data.get('talla')
        if talla <= 0:
            raise ValidationError("La talla debe ser un valor positivo.")
        return talla

    def clean_temperatura(self):
        temperatura = self.cleaned_data.get('temperatura')
        if temperatura < 35 or temperatura > 42:
            raise ValidationError("La temperatura debe estar entre 35 y 42 grados Celsius.")
        return temperatura

    def clean_frecuencia_cardiaca(self):
        frecuencia_cardiaca = self.cleaned_data.get('frecuencia_cardiaca')
        if frecuencia_cardiaca <= 0:
            raise ValidationError("La frecuencia cardíaca debe ser un valor positivo.")
        return frecuencia_cardiaca

    def clean_frecuencia_respiratoria(self):
        frecuencia_respiratoria = self.cleaned_data.get('frecuencia_respiratoria')
        if frecuencia_respiratoria <= 0:
            raise ValidationError("La frecuencia respiratoria debe ser un valor positivo.")
        return frecuencia_respiratoria

    def clean_nivel_glucosa(self):
        nivel_glucosa = self.cleaned_data.get('nivel_glucosa')
        if nivel_glucosa <= 0:
            raise ValidationError("El nivel de glucosa debe ser un valor positivo.")
        return nivel_glucosa

    def clean_saturacion(self):
        saturacion = self.cleaned_data.get('saturacion')
        if saturacion < 0 or saturacion > 100:
            raise ValidationError("La saturación debe estar entre 0 y 100%.")
        return saturacion