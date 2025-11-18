from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
#CRUD

#CREATE TODO
class CreateTodoView(generic.CreateView):
    model = models.TodoModel
    form_class = forms.TodoForm
    template_name = 'todo/todo_create.html'
    success_url = '/todo_list/'


#TODO LIST
def todoListView(request):
    if request.method == 'GET':
        todo = models.TodoModel.objects.all().order_by('-id')    
    return render(request, 'todo/todo_list.html', {'todo': todo})


#TODO UPDATE

class TodoUpdateView(generic.UpdateView):
    model = models.TodoModel
    form_class = forms.TodoForm
    template_name = 'todo/todo_update.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TodoUpdateView, self).form_valid(form=form)
        


#DELETE TODO
class TodoDeleteView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.TodoModel, id=todo_id)
