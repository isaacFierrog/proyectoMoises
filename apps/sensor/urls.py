from django.urls import path
from .views import listar_sensores, eliminar_sensor


urlpatterns = [
    path('', listar_sensores, name='listado'),
    path('eliminar/<id>/', eliminar_sensor, name='eliminar')
]
