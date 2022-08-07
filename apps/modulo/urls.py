from django.urls import path
from .views import crear_modulo, eliminar_modulo, ModuloListCreateAPIView


urlpatterns = [
    path('crear/', crear_modulo, name='crear'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar'),
    path('api/', ModuloListCreateAPIView.as_view(), name='listar-crear')
]