# models.py
from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Archivo(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
