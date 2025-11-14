from django.urls import path
from . import views


urlpatterns = [
    path('', views.filmListView, name='film_list'),
    path('film_list/<int:id>/', views.filmDetailView, name='film_detail'),
    path('search/', views.searchView, name='search'),
]