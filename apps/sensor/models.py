from django.db import models


class SensorModel(models.Model):
    id = models.CharField(
        'Identificador de sensor',
        max_length=5,
        primary_key=True,
        blank=True
    )
    estado = models.BooleanField(
        'Estado del sensor',
        default=True
    )
    fecha_cracion = models.DateField(
        'Fecha en que se creo el sensor',
        auto_now_add=True,
        auto_now=False
    )
    modulo = models.ForeignKey(
        'modulo.ModuloModel', 
        on_delete=models.CASCADE,
        blank=True,
        related_name='sensores'
    )
    
    class Meta:
        verbose_name = 'sensor'
        verbose_name_plural = 'sensores'
        db_table = 'sensor'
        
    def __str__(self):
        return f'<Sensor: {self.id}>'
    
    
class ValorModel(models.Model):
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
    estado = models.BooleanField(
        'Estado de la medicion',
        default=True
    )
    fecha_medicion = models.DateField(
        'Fecha en que se tomo la medida',
        auto_now_add=True,
        auto_now=False
    )
    
    class Meta:
        verbose_name = 'valor'
        verbose_name_plural = 'valores'
        db_table = 'valor'
        
    def __str__(self):
        return f'<Valor: {self.medida}>'