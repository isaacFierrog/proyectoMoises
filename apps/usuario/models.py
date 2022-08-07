from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, apellido, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        usuario = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellido=apellido
        )
        usuario.set_password(password)
        usuario.save()
        
        return usuario
    
    def create_superuser(self, email, nombre, apellido, password):
        usuario = self.create_user(
            email=email,
            nombre=nombre,
            apellido=apellido,
            password=password
        )
        usuario.administrador = True
        usuario.save()
        
        return usuario



class UsuarioModel(AbstractBaseUser):
    email = models.EmailField(
        'Correo del usuario',
        max_length=150,
        unique=True
    )
    nombre = models.CharField(
        'Nombre del usuario',
        max_length=150
    )
    apellido = models.CharField(
        'Apellido del usuario',
        max_length=150
    )
    activo = models.BooleanField(
        'Estado del usuario',
        default=True
    )
    administrador = models.BooleanField(
        '¿El usuario es administrador?',
        default=False
    )
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellido']
    
    def __str__(self):
        return f'Usuario: {self.nombre} {self.apellido}'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.administrador

