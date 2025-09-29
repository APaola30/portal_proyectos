from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto, Archivo
from .forms import ProyectoForm
from django.contrib import messages
from .forms import ProyectoForm, ArchivoForm

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

            
            return redirect('proyecto_lista')
    else:
        form = ProyectoForm()

    return render(request, 'projects/proyecto_form.html', {'form': form})



def proyecto_eliminar(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == "POST":
        proyecto.delete()
        return redirect('proyecto_lista')
    return render(request, 'projects/proyecto_confirm_delete.html', {'proyecto': proyecto})

def proyecto_editar(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == "POST":
        proyecto_form = ProyectoForm(request.POST, instance=proyecto)
        archivos = request.FILES.getlist('archivos')

        archivos_invalidos = []  # lista para archivos no válidos

        if proyecto_form.is_valid():
            # Primero validamos los archivos
            for archivo in archivos:
                archivo_form = ArchivoForm(files={'archivo': archivo})
                if not archivo_form.is_valid():
                    archivos_invalidos.append(f"{archivo.name}: {archivo_form.errors['archivo'][0]}")
            
            if archivos_invalidos:
                # Mostrar mensajes de error y no guardar nada
                for msg in archivos_invalidos:
                    messages.error(request, f"No se pudo subir {msg}")
            else:
                # Guardamos proyecto y archivos solo si todos son válidos
                proyecto_form.save()
                for archivo in archivos:
                    Archivo.objects.create(proyecto=proyecto, archivo=archivo)
                
                return redirect('proyecto_detalle', pk=proyecto.pk)
        else:
            messages.error(request, "Error al actualizar el proyecto.")
    else:
        proyecto_form = ProyectoForm(instance=proyecto)

    return render(request, 'projects/proyecto_editar.html', {
        'proyecto_form': proyecto_form,
        'proyecto': proyecto
    })


def archivo_eliminar(request, pk):
    archivo = get_object_or_404(Archivo, pk=pk)
    proyecto_pk = archivo.proyecto.pk
    archivo.delete()
    messages.success(request, "Archivo eliminado correctamente.")
    return redirect('proyecto_editar', pk=proyecto_pk)
def home(request):
    return render(request, 'projects/home.html')