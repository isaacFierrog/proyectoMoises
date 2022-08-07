from django.shortcuts import redirect, render
from rest_framework.generics import ListCreateAPIView
from .models import ModuloModel
from .serializers import ModuloSerializer    


class ModuloListCreateAPIView(ListCreateAPIView):
    serializer_class = ModuloSerializer
    queryset = ModuloModel.objects.all()

    
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
    
