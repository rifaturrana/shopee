from django.urls import path
from .views import *

urlpatterns = [

       path('', all_products, name='all_products'),
       path('<int:product_id>/', product_details, name='product_details'),
]