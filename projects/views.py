from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Tag,Review
from .forms import  ProjectModelForm
from django.shortcuts import redirect



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

def createProject(request):
    form = ProjectModelForm()
    if request.method =='POST':
        # print(request.POST)
        form = ProjectModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/projects_form.html',context)



def updateProject(request,pk):
    project = Project.objects.get(id = pk)
    form = ProjectModelForm(instance=project)
    if request.method =='POST':
        # print(request.POST)
        form = ProjectModelForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/projects_form.html',context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'projects/delete.html',context)