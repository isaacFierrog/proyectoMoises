from dataclasses import fields
from django import forms
from .models import ValorModel


class ValorForm(forms.ModelForm):
    class Meta:
        model = ValorModel
        fields = ('medida',)
        exclude = (
            'fecha_modificacion',
            'fecha_creacion',
            'estado'
        )