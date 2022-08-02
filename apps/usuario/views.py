import json
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, FormView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .models import UsuarioModel
from .forms import UsuarioForm, UsuarioLoginForm


class UsuarioLoginFormView(FormView):
    template_name = 'login.html'
    form_class = UsuarioLoginForm
    success_url = reverse_lazy('home:home')
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.get_success_url())
        else: 
            return super(UsuarioLoginFormView, self).dispatch(request, *args, **kwargs)
        
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(UsuarioLoginFormView, self).form_valid(form)


class UsuarioCreateView(CreateView):
    model = UsuarioModel
    template_name = 'usuario/usuario_crear.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:listar')
    
    
class UsuarioListView(ListView):
    model = UsuarioModel
    template_name = 'usuario/usuario_listar.html'
    
    def get_queryset(self):
        return self.model.objects.filter(activo=True)
    
    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            lista_usuarios = [] 
            
            for usuario in self.get_queryset():
                data_usuario = {}
                data_usuario['id'] = usuario.id
                data_usuario['nombre'] = usuario.nombre
                data_usuario['apellido'] = usuario.apellido
                data_usuario['email'] = usuario.email
                data_usuario['activo'] = usuario.activo
                lista_usuarios.append(data_usuario)
                
            data = json.dumps(lista_usuarios )
            return HttpResponse(data, 'application/json')
        
        return render(request, self.template_name)
    
    
class UsuarioUpdateView(UpdateView):
    model = UsuarioModel
    template_name = 'usuario/usuario_crear.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:listar')
    
    
class UsuarioDeleteView(DeleteView):
    model = UsuarioModel
    template_name = 'usuario/usuario_eliminar.html'
    
    def post(self, request, pk=None, *args, **kwargs):
        object = self.model.objects.get(id=pk)
        object.activo = False
        object.save()
        
        return redirect('usuarios:listar')

    
def usuario_logout(request):
    logout(request)
    return redirect('login')