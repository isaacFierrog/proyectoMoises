from django.urls import path
from .views import eliminar_modulo, ModuloListCreateAPIView


urlpatterns = [
    path('eliminar/<id>/', eliminar_modulo, name='eliminar'),
    path('api/', ModuloListCreateAPIView.as_view(), name='listar-crear')
]