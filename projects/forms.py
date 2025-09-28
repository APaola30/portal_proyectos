# forms.py
from django import forms
from .models import Proyecto, Archivo

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion']

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']
        widgets = {
            'archivo': forms.ClearableFileInput(attrs={'multiple': True})
        }
