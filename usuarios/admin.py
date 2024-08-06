from django.contrib import admin

# Register your models here.
# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioVai, Rol, Cargo

class UsuarioVaiAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('telefono', 'rol', 'cargo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('telefono', 'rol', 'cargo')}),
    )


admin.site.register(UsuarioVai)
admin.site.register(Rol)
admin.site.register(Cargo)