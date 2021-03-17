from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):

    numbers = []
    total = 0

    tasks = Task.objects.all()
    category_list = [
        'All',
        'Travel',
        'Music',
        'Work',
        'Home',
        'Study',
        'Art',
        'Shopping',
        'Others'
    ]
    
    for x in category_list:
        category_task_count = Task.objects.filter(category = x).count()
        numbers.append(category_task_count)

    for num in numbers:
        total = total + num

    data = zip(category_list, numbers)
        
    context = {
        'tasks': tasks,
        'data': data,
        'total': total
    }

    return render(request, 'tasks/index.html', context)


def show_category(request, pk):

    created_list = []

    if pk == 'All':
        tasks = Task.objects.all()
        for task in tasks:
            created = task.created
            created_list.append(created)
    else:
        tasks = Task.objects.filter(category=pk)
        for task in tasks:
            created = task.created
            created_list.append(created)

    tasks_number = tasks.count()

    img = pk.lower()
    category_name = pk.capitalize()
    data = zip(tasks, created_list)



    context = {
        'data':data,
        'img': img,
        'category_name': category_name,
        'tasks_number': tasks_number
    }

    return render(request, 'tasks/show_category.html', context)


def updateTask(request, pk, page):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/show_category/' + page + '/')

    context = { 
        'form':form, 
        'page': page
        }

    return render(request, 'tasks/update.html', context)


def deleteTask(request, pk, page):
	task = Task.objects.get(id=pk)

	if request.method == 'POST':
		task.delete()
		return redirect('/show_category/' + page + '/')

	context = {
            'task': task,
            'page': page
        }

	return render(request, 'tasks/delete_task.html', context)


def createTask(request, page):

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.category = page
            instance.save()
            return redirect('/show_category/' + page + '/')

    form = TaskForm()

    context = {
        'form': form,
        'page': page    
    }

    return render(request, 'tasks/create_task.html', context)





