from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#CRUD

#CREATE TODO
def createTodoView(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm()
    
    return render(request, 'todo/todo_create.html', {'form': form})

#TODO LIST
def todoListView(request):
    if request.method == 'GET':
        todo = models.TodoModel.objects.all().order_by('-id')    
    return render(request, 'todo/todo_list.html', {'todo': todo})


#TODO UPDATE
def updateTodoView(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo_id)
        if form.is_valid:
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm(instance=todo_id)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo_id': todo_id})

#DELETE TODO
def deleteTodo(request, id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    todo_id.delete()
    return redirect('todo_list')
