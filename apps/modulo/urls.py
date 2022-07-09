from django.urls import path
from .views import listar_modulos, crear_modulo, eliminar_modulo


urlpatterns = [
    path('', listar_modulos, name='listado'),
    path('crear/', crear_modulo, name='crear'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar')
]
