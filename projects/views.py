# views.py
from django.shortcuts import render, redirect
from .forms import ProyectoForm, ArchivoForm
from .models import Proyecto, Archivo

def crear_proyecto(request):
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST)
        archivo_form = ArchivoForm(request.POST, request.FILES)
        if proyecto_form.is_valid() and archivo_form.is_valid():
            proyecto = proyecto_form.save()
            archivos = request.FILES.getlist('archivo')
            for archivo in archivos:
                Archivo.objects.create(proyecto=proyecto, archivo=archivo)
            return redirect('proyecto_detalle', pk=proyecto.pk)
    else:
        proyecto_form = ProyectoForm()
        archivo_form = ArchivoForm()
    return render(request, 'crear_proyecto.html', {'proyecto_form': proyecto_form, 'archivo_form': archivo_form})
