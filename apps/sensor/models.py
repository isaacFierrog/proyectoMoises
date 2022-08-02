from django.db import models
from apps.general.models.modelos_generales import BaseModel


class SensorModel(BaseModel):
    id = models.CharField(
        'Identificador de sensor',
        max_length=5,
        primary_key=True,
        blank=True
    )
    conexion = models.BooleanField(
        'Estado de la conexion del sensor',
        default=True
    )
    modulo = models.ForeignKey(
        'modulo.ModuloModel', 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='sensores',
        default=None
    )
    
    class Meta:
        verbose_name = 'sensor'
        verbose_name_plural = 'sensores'
        db_table = 'sensor'
        
    def __str__(self):
        return f'<Sensor: {self.id}>'
    
    
class ValorModel(BaseModel):
    id = models.AutoField(
        'Identificador de valor',
        primary_key=True
    )
    medida = models.PositiveIntegerField(
        'Valor de la medida del sensor'
    )
    sensor = models.ForeignKey(
        'sensor.SensorModel', 
        on_delete=models.CASCADE,
        related_name='valores'
    )
    
    class Meta:
        verbose_name = 'valor'
        verbose_name_plural = 'valores'
        db_table = 'valor'
        
    def __str__(self):
        return f'<Valor: {self.medida}>'