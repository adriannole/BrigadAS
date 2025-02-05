from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Especialidad, Paciente, User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'especialidad', 'is_admin', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('especialidad',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('especialidad',)}),
    )

admin.site.register(Especialidad)
admin.site.register(Paciente)
admin.site.register(User, CustomUserAdmin)