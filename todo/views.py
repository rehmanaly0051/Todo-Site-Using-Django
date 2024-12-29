from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages 

from .forms import TodoForm
from .models import Todo

def index(response):
    item_list = Todo.objects.order_by('-date')
    
    if response.method == 'POST':
        form = TodoForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = TodoForm()
    
    page = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(response, 'todo/index.html', page) 


def add(response):
    if response.method == 'POST':
        form = TodoForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = TodoForm()
    page = {
        'forms': form, 'title': 'Add TODO'}
    return render(response, 'todo/index.html', page)  

def edit(response, item_id):
    item = get_object_or_404(Todo, id=item_id)
    if response.method == 'POST':
        form = TodoForm(response.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = TodoForm(instance=item)
    
    page = {
        'forms': form,
        'title': 'Edit TODO',
        'list': Todo.objects.order_by('-date'),  
    }
    return render(response, 'todo/index.html', page)

def remove(response, item_id):
    try:
        item = Todo.objects.get(id=item_id)
        item.delete()
        messages.info(response, 'Item has been removed.')
    except Todo.DoesNotExist:    
        messages.error(response, 'Item does not exist!')
    return redirect('index')  