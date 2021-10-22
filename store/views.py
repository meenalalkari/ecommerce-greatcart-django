from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
from category.models import Category
# Create your views here.
def store(request,category_slug = None):
    if category_slug != None:
        categories = None
        products = None
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category = categories,is_available=True)
    else:
        products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)

def product_detail(request,category_slug=None,product_slug=None):
    products = None
    categories = None
    categories = get_object_or_404(Category,slug = category_slug)
    if categories != None:
        products = Product.objects.filter(category = categories,slug = product_slug)
        context = {'products':products}
        return render(request,'store/product_detail.html',context)
