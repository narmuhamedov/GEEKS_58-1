from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/', views.todoListView, name='todo_list'),
    path('todo_list/<int:id>/update/', views.updateTodoView, name='update_todo'),
    path('todo_list/<int:id>/delete/', views.deleteTodo, name='delete_todo'),
    path('create_todo/', views.createTodoView, name='create_todo')
]