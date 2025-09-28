from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Archivo
from .forms import ProyectoForm

def proyecto_lista(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'projects/proyecto_list.html', {'proyectos': proyectos})

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'projects/proyecto_detail.html', {'proyecto': proyecto})

def proyecto_crear(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        archivos = request.FILES.getlist('archivos')
        if form.is_valid():
            proyecto = form.save()
            for f in archivos:
                proyecto.archivos.create(archivo=f)
            return redirect('proyecto_lista')
    else:
        form = ProyectoForm()
    return render(request, 'projects/proyecto_form.html', {'form': form})


def home(request):
    return render(request, 'projects/home.html')