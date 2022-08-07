from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.usuario.views import UsuarioLoginFormView, usuario_logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.home.urls', 'home')),),
    # Autenticacion
    path('accounts/login/', UsuarioLoginFormView.as_view(), name='login'),
    path('logout/', login_required(usuario_logout), name='logout'),
    # Procesos
    path('modulos/', include(('apps.modulo.urls', 'modulos'))),
    path('sensores/', include(('apps.sensor.urls', 'sensores'))),
    path('usuarios/', include(('django.contrib.auth.urls', 'usuarios')))
]
