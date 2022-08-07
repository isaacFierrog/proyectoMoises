from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UsuarioModel


class UsuarioLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UsuarioLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password'].widget.attrs['class'] = 'form-control'


class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña',
        'id': 'password1',
        'required': 'required'
    }))
    password2 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña nuevamente',
        'id': 'password2',
        'required': 'required'
    }))
    
    class Meta: 
        model = UsuarioModel
        fields = ('email', 'nombre', 'apellido', 'administrador')
        labels = {
            'administrador': '¿Es administrador?'
        }
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Correo electronico'
            }),
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Nombre del usuario'
            }),
            'apellido': forms.TextInput(attrs={
                'placeholder': 'Apellido del usuario'
            }),
            'administrador': forms.CheckboxInput()
        }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', None)
        password2 = self.cleaned_data.get('password2', None)
        
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        
        return password2
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        
        return user