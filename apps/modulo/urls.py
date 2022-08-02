from django.urls import path
from .views import eliminar_modulo, ModuloListView


urlpatterns = [
    path('', ModuloListView.as_view(), name='listado'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar')
]
