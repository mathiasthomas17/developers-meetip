from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tag,Review



# Create your views here.
def projects(request):
    projects = Project.objects.all()
    print(projects)
    context =  {'projects':projects}
    return render(request,'projects/projects.html',context)
def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tag.all()
    return render(request,'projects/single-projects.html',{'project':projectObj})

