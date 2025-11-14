from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_productsView, name='all_prod'),
    path('car_products/', views.autoProductsView, name='car'),
]