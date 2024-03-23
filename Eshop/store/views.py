from django.shortcuts import render,HttpResponse
from .models.product import Product
# Create your views here.
def home(request):
    products = Product.get_all_product()
    print(products)
    return render(request,'index.html', {"products":products})