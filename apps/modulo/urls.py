from django.urls import path
<<<<<<< HEAD
from .views import listar_modulos, crear_modulo, eliminar_modulo, ModuloListCreateAPIView


urlpatterns = [
    path('', listar_modulos, name='listado'),
    path('crear/', crear_modulo, name='crear'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar'),
    path('api/', ModuloListCreateAPIView.as_view(), name='listar-crear')
=======
from .views import eliminar_modulo, ModuloListView


urlpatterns = [
    path('', ModuloListView.as_view(), name='listado'),
    path('eliminar/<id>/', eliminar_modulo, name='eliminar')
>>>>>>> 83aa6e4be512664272abd6a805f129a5130b92c3
]
