from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def all_products(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request,'product/all_products.html',{
        'products':products,
        'categories':categories
    })

def product_details(request,product_id):
    try:
      product=Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse("Product Not Found")
    return render(request,'product/product_details.html',{
        'product':product
    })