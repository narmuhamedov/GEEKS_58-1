from django.urls import path
from . import views

urlpatterns = [
    path('hello_world/', views.hello_world_view, name='hello_world'),
    path('blog_list_test/', views.blog_list_view, name='blog_list'),
    path('random_blog/', views.blog_list_random_view, name='random_blog'),
]
