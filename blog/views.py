from django.shortcuts import render
from django.http import HttpResponse
import random

def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World')

def blog_list_view(request):
    if request.method == 'GET':
        blogs = ['Новости об образовании', 'Новости об контракте', 
                 'Новости об GEEKCOINS']    
        result = "Список новостей:\n" + "\n".join(blogs)
        return HttpResponse(result)
    

def blog_list_random_view(request):
    if request.method == 'GET':
        blogs_random = ['Новости об Университете', 'Новости об Игровой площадки', 
                 'Новости об Институтах прикладных наук']    
        return HttpResponse(random.choice(blogs_random))