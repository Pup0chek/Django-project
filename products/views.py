from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'products/index.html', {"Title":"LOLOLOLO"})

def products(request):
    return render(request, 'products/products.html')