from asyncio import tasks
from wsgiref.headers import tspecials
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse


from .models import *
from .forms import *
# Create your views here.
def Home(request):
    tasks=Task.objects.all()
    form=TaskForm()

    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    data={
        'tasks':tasks,
        'form':form
    }
    return render(request,'list.html',data)

def Update(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method=="POST":
        form=TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()

            return redirect('/')
    data={'form':form,
        'task':task
    }
    return render(request,'update.html',data)

def Delete(request,pk):
    item=Task.objects.get(id=pk)

    if request.method=="POST":
        item.delete()
        return redirect('/')
    data={
        'item':item,
    }
    return render(request,'delete.html',data)