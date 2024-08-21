# Generated by Django 5.1 on 2024-08-16 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('apellidos_nombres', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('sector', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('afiliado_seguro', models.BooleanField(default=False)),
                ('discapacidad', models.BooleanField(default=False)),
                ('porcentaje_discapacidad', models.FloatField(blank=True, null=True)),
                ('tipo_discapacidad', models.CharField(blank=True, max_length=100, null=True)),
                ('antecedentes_patologicos_personales', models.TextField(blank=True, null=True)),
                ('antecedentes_patologicos_familiares', models.TextField(blank=True, null=True)),
                ('presion_arterial', models.CharField(blank=True, max_length=10, null=True)),
                ('peso', models.FloatField(blank=True, null=True)),
                ('talla', models.FloatField(blank=True, null=True)),
                ('imc', models.FloatField(blank=True, null=True)),
                ('diagnostico_imc', models.CharField(blank=True, max_length=50, null=True)),
                ('temperatura', models.FloatField(blank=True, null=True)),
                ('frecuencia_cardiaca', models.IntegerField(blank=True, null=True)),
                ('frecuencia_respiratoria', models.IntegerField(blank=True, null=True)),
                ('nivel_glucosa', models.FloatField(blank=True, null=True)),
                ('saturacion', models.FloatField(blank=True, null=True)),
                ('diagnostico', models.TextField(blank=True, null=True)),
                ('cie_10', models.CharField(blank=True, max_length=100, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('responsable', models.CharField(max_length=100)),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.especialidad')),
            ],
        ),
    ]
