from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

class ProjectFileForm(forms.Form):
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=True
    )

    def clean_files(self):
        files = self.files.getlist('files')  # obtenemos todos los archivos
        for f in files:
            if not f.name.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf')):
                raise forms.ValidationError('Solo se permiten imágenes o PDFs.')
        return files
