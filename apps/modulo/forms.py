from django import forms
from .models import ModuloModel


class ModuloForm(forms.ModelForm):
    class Meta:
        model = ModuloModel
        fields = ['id']