from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import SensorModel, ValorModel
from apps.modulo.models import ModuloModel


# class SensorView(ListView):
#     model = SensorModel
#     queryset = SensorModel.objects.filter(estado=True)
#     template_name = 'sensor/sensor.html'
#     context_object_name = 'sensores'

def listar_sensores(request):
    sensores = SensorModel.objects.filter(estado=True)
    modulos = ModuloModel.objects.filter(estado=True)
    
    if(request.method == 'POST'):
        id_sensor = hex(sensores.count()).split('0x')[1]
        SensorModel.objects.create(id=id_sensor)
        
        return redirect('modulos:listado')
    
    return render(request, 'sensor/sensor_listar.html', {
        'sensores': sensores,
        'modulos': modulos
    })