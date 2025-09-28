from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Archivo
from .forms import ProyectoForm
from django.contrib import messages

def proyecto_lista(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'projects/proyecto_list.html', {'proyectos': proyectos})

def proyecto_detalle(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    return render(request, 'projects/proyecto_detail.html', {'proyecto': proyecto})

def proyecto_crear(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        archivos = request.FILES.getlist('archivos')  # 'archivos' es el name del input en tu template

        if form.is_valid():
            proyecto = form.save()

            for archivo in archivos:
                # Validación de tipo
                if archivo.content_type not in ['application/pdf', 'image/jpeg', 'image/png']:
                    messages.error(request, f"El archivo {archivo.name} no es PDF ni imagen.")
                    proyecto.delete()  # opcional: eliminar proyecto si hay error
                    return redirect('proyecto_crear')

                # Validación de tamaño (max 5MB)
                if archivo.size > 5 * 1024 * 1024:
                    messages.error(request, f"El archivo {archivo.name} excede 5MB.")
                    proyecto.delete()
                    return redirect('proyecto_crear')

                Archivo.objects.create(proyecto=proyecto, archivo=archivo)

            messages.success(request, "Proyecto creado correctamente.")
            return redirect('proyecto_list')
    else:
        form = ProyectoForm()

    return render(request, 'projects/proyecto_form.html', {'form': form})

def home(request):
    return render(request, 'projects/home.html')