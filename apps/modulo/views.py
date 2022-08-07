from django.shortcuts import redirect, render
<<<<<<< HEAD
from rest_framework.generics import ListCreateAPIView
from .models import ModuloModel
from .serializers import ModuloSerializer    


class ModuloListCreateAPIView(ListCreateAPIView):
    serializer_class = ModuloSerializer
    queryset = ModuloModel.objects.all()

=======
from django.views.generic import ListView
from rest_framework.generics import CreateAPIView
from .models import ModuloModel
from .serializers import ModuloSerializer


class ModuloCreateAPIView(CreateAPIView):
    serializer_class = ModuloSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ModuloListView(ListView):
    model = ModuloModel
    queryset = ModuloModel.objects.all().filter(estado=True)
    template_name = 'modulo/modulo_listar.html' 
    context_object_name = 'modulos'   
>>>>>>> 83aa6e4be512664272abd6a805f129a5130b92c3
    
    def post(self, request, *args, **kwargs):
        numero_modulos = ModuloModel.objects.all().count()
        id_modulo = hex(numero_modulos).split('0x')[1]
        
        ModuloModel.objects.create(id=id_modulo)
        
        return redirect('modulos:listado')


def eliminar_modulo(request, id):
    modulo = ModuloModel.objects.filter(id=id).first()
    modulo.estado = False
    modulo.save()
    
    return redirect('modulos:listado')
    
