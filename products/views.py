from django.shortcuts import render, HttpResponse
from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'test_title', #placeholder (еще есть шаблонные теги, которые скрывают или показывают текст в зависимоти от бул)
    }
    return render(request, 'products/index.html', context=context)

def products(request):
    context = {
        'title': 'Store - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context=context)