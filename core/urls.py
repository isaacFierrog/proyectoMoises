from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.home.urls', 'home'))),
    path('modulos/', include(('apps.modulo.urls', 'modulos'))),
    path('sensores/', include(('apps.sensor.urls', 'sensores')))
]
