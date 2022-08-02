from django.db import models


class BaseModel(models.Model):
    estado = models.BooleanField(
        'Estado del elemento',
        default=True
    )
    fecha_modificacion = models.DateField(
        'Fecha en la que se edito el elemento',
        auto_now_add=True
    )
    fecha_creacion = models.DateField(
        'Fecha en que se creo el elemento',
        auto_now=True,
        auto_now_add=False
    )
    
    class Meta:
        abstract = True