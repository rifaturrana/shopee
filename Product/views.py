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
    if request.method=="POST":
        review=Review.objects.create(product=product,user=request.user,rating=request.POST['rating'],review=request.POST['review'])
        review.save()
    reviews=Review.objects.filter(product=product)
    average_rating=0
    if reviews:
        average_rating=sum([review.rating for review in reviews])/len(reviews)
        average_rating=round(average_rating,1)

    return render(request,'product/product_details.html',{
        'product':product,
         'reviews': reviews, 
         'average_rating': average_rating
    })