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

    def clean_archivo(self):
        archivo = self.cleaned_data.get('archivo')
        if archivo:
            # Tipos permitidos
            valid_mime_types = ['application/pdf', 'image/jpeg', 'image/png', 'image/jpg']
            if archivo.content_type not in valid_mime_types:
                raise forms.ValidationError('Solo se permiten archivos PDF o imágenes (JPG, PNG).')
            
            # Tamaño máximo opcional (por ejemplo, 5 MB)
            if archivo.size > 5*1024*1024:
                raise forms.ValidationError('El archivo no puede ser mayor a 5 MB.')
        return archivo