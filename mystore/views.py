from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mystore/index.html')

def product(request):
    return render(request, 'mystore/products.html')

def product_details(request):
    return render(request, 'mystore/product_details.html')

def contact(request):
    return render(request, 'mystore/contact.html')

def login(request):
    return render(request, 'mystore/login.html')

def register(request):
    return render(request, 'mystore/register.html')