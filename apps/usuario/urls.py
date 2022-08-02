from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import UsuarioCreateView
from .views import UsuarioListView
from .views import UsuarioUpdateView
from .views import UsuarioDeleteView


urlpatterns = [
    path('crear/', login_required(UsuarioCreateView.as_view()), name='crear'),
    path('listar/', login_required(UsuarioListView.as_view()), name='listar'),
    path('editar/<int:pk>/', login_required(UsuarioUpdateView.as_view()), name='editar'),
    path('eliminar/<int:pk>/', login_required(UsuarioDeleteView.as_view()), name='eliminar')
]