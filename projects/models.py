from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo

class Archivo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='archivos')
    archivo = models.FileField(upload_to='archivos/')

    def __str__(self):
        return f"{self.archivo.name}"
