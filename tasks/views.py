from django.shortcuts import render,redirect
from .models import *
from .forms import *


def index(request):
    all_task = task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm (request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')

    data = {'task':all_task , 'form' : form }
    return render(request,'base.html',data)


def updateTask(request,pk):
    all_task = task.objects.get(id=pk)
    form = TaskForm(instance=all_task)

    if request.method =='POST':
        form = TaskForm(request.POST, instance=all_task)
        if form.is_valid():
            form.save()
        return redirect ('/')
    context = {'form':form}
    return render (request,'update_task.html',context)

def deleteTask(request, pk) :
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request,'delete.html',context)
