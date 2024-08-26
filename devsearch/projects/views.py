from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {'title':'projectA', 'description':'projectA description'},
    {'title':'projectB', 'description':'projectB description'}
]
# Create your views here.
def projects(request):
    context = {
        'projects':projectsList
    }
    print(projects)
    return render(request, "projects/projects.html", context)

def project(request, pk):
    # return HttpResponse("Page for project with id:{}".format(pk))
    return render(request, "projects/single-project.html")