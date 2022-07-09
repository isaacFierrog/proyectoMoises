from django.shortcuts import redirect, render
from .models import ModuloModel
    
    
def listar_modulos(request):
    modulos = ModuloModel.objects.all()
    
    if request.method == 'POST':
        id_modulo = hex(modulos.count()).split('0x')[1]
        ModuloModel.objects.create(id=id_modulo)
        
        return redirect('modulos:listado')
    
    return render(request, 'modulo/modulo_listar.html', {
        'modulos': modulos.filter(estado=True)
    })


def crear_modulo(request):
    if request.method == 'POST':
        pass


def eliminar_modulo(request, id):
    modulo = ModuloModel.objects.filter(id=id).first()
    modulo.estado = False
    modulo.save()
    
    return redirect('modulos:listado')
    
