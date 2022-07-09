from django.db import models


class ModuloModel(models.Model):
    id = models.CharField(
        'Identificador de modulo',
        max_length=5,
        primary_key=True,
        blank=True
    )
    estado = models.BooleanField(
        'Estado del modulo',
        default=True
    )
    fecha_cracion = models.DateField(
        'Fecha en que se creo el modulo',
        auto_now_add=True,
        auto_now=False
    )
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'
        db_table = 'modulo'
        
    def __str__(self):
        return f'<Modulo: {self.id}>'