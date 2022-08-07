from django.urls import path
from .views import listar_modulos, crear_modulo, eliminar_modulo, ModuloListCreateAPIView


urlpatterns = [
    path('', listar_modulos, name='listado'),
    path('crear/', crear_modulo, name='crear'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar'),
    path('api/', ModuloListCreateAPIView.as_view(), name='listar-crear')
]
