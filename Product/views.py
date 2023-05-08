from django.shortcuts import render
from .models import *
# Create your views here.

def all_products(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,'product/all_products.html',{
        'products':products,
        'categories':categories
    })