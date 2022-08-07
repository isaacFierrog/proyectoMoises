from lib2to3.pytree import Base
from django.db import models
from apps.general.models.modelos_generales import BaseModel


class ModuloModel(BaseModel):
    sensor_id = models.CharField(
        'Identificador del modulo',
        max_length=12
    )
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'
        db_table = 'modulo'
        
    def __str__(self):
        return f'<Modulo: {self.id}>'