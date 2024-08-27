from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Project
from projects.forms import ProjectForm

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    print(projects)
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    context = {"project": projectObj}
    return render(request, "projects/single-project.html", context)

def createProject(request):
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.Files)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form  = ProjectForm()
    context = {
        "form":form
    }
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.files, instance=project,)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm(instance=project)
    context = {
        "form":form
    }
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    print("hellooooo")
    print(request.method)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    form = ProjectForm(instance=project)
    context = {
        "object":project
    }
    return render(request, "projects/delete_popup.html", context)