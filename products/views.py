from django.shortcuts import render
from . import models


#Все товары
def all_productsView(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        return render(request, 'products/all_products.html', {'products': products})

#Для авто
def autoProductsView(request):
    if request.method == 'GET':
        car_products = models.Product.objects.filter(tags__name='#для авто')
        return render(request, 'products/car_products.html', {'car_products':car_products})
