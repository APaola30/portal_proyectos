from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectForm, ProjectFileForm
from .models import Project, ProjectFile

def project_create(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        file_form = ProjectFileForm(request.POST, request.FILES)
        if project_form.is_valid() and file_form.is_valid():
            project = project_form.save()
            for f in request.FILES.getlist('files'):
                ProjectFile.objects.create(project=project, file=f)
            return redirect('project_list')
    else:
        project_form = ProjectForm()
        file_form = ProjectFileForm()
    return render(request, 'projects/project_form.html', {
        'project_form': project_form,
        'file_form': file_form
    })

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})
