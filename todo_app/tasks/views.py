from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    return render(request, "index.html")

def task_list(request):
    tasks = Task.objects.all()

    context = {"tasks": tasks,

               }
    return render(request, "task_list.html", context)

def create_task(request):
    form = TaskForm()

    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm()
    context = {"form": form}
    return render(request, "form.html", context)

def updateTask(request, pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/list')
    context = {'form': form}
    return render(request, 'update_task.html', context)
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect('/list')
    context = {'item': item}
    return render(request, 'delete.html', context)