from django.urls import path
from .views import listar_sensores


urlpatterns = [
    path('', listar_sensores, name='listado')
]
