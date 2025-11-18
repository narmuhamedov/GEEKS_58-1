from django.urls import path
from . import views


urlpatterns = [
    path('', views.FilmListView.as_view(), name='film_list'),
    path('film_list/<int:id>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('search/', views.SearchView.as_view(), name='search'),
]