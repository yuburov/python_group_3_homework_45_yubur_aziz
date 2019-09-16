from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import TaskForm
from webapp.models import Task, STATUS_CHOISES

def index_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST':
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        values = request.POST.getlist('checkbox')

        Task.objects.filter(id__in=values).delete()
        return render(request, 'index.html', context)



def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'task': task
    })

def task_create_view(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'create.html', context={
            'status_choises': STATUS_CHOISES, 'form': form
        })
    elif request.method == 'POST':
            form = TaskForm(data=request.POST)
            if form.is_valid():
                task = Task.objects.create(description = form.cleaned_data['description'],
                specific = form.cleaned_data['specific'], status = form.cleaned_data['status'],
                date_of_completion = form.cleaned_data['date_of_completion'])
                return redirect('task_view', pk=task.pk)

            else:
                return render(request, 'create.html', context={'status_choises': STATUS_CHOISES, 'form': form})

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(data={
            'description': task.description,
            'specific': task.specific,
            'status': task.status,
            'date_of_completion':task.date_of_completion
        })
        return render(request, 'update.html', context={'form':form, 'task': task, 'status_choises': STATUS_CHOISES})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.specific= form.cleaned_data['specific']
            task.status = form.cleaned_data['status']
            task.date_of_completion = form.cleaned_data['date_of_completion']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'task': task, 'status_choises': STATUS_CHOISES})

def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return  redirect('index')


