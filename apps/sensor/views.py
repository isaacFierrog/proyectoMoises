from django.shortcuts import redirect, render
from .models import SensorModel, ValorModel
from apps.modulo.models import ModuloModel


def listar_sensores(request):
    sensores = SensorModel.objects.filter(estado=True)
    modulos = ModuloModel.objects.filter(estado=True)
    
    if(request.method == 'POST'):
        id_modulo = request.POST['modulo']
        id_sensor = hex(sensores.count()).split('0x')[1]
        modulo = ModuloModel.objects.filter(id=id_modulo).first()
        SensorModel.objects.create(
            id=id_sensor,
            modulo=modulo
        )
        
        print(request.POST)
        
        return redirect('sensores:listado')
    
    return render(request, 'sensor/sensor_listar.html', {
        'sensores': sensores,
        'modulos': modulos
    })
    
    
def eliminar_sensor(request, id):
    sensor = SensorModel.objects.filter(id=id).first()
    sensor.estado = False
    sensor.save()
    
    return redirect('sensores:listado')