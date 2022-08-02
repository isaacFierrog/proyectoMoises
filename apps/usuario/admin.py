from django.contrib import admin
from .models import UsuarioModel


class UsuarioAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'email','nombre', 'apellido')


admin.site.register(UsuarioModel, UsuarioAdmin)