from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,CartItem
from store.models import Product, Product_Variation
from django.http import HttpResponse
# Create your views here.

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        print(request.POST)
        for item in request.POST:
            print('in for loop')
            key = item
            value = request.POST[key]
            print(key , value)
            try:
                print('in try')
                variation = Product_Variation.objects.get(product = product, variation_category__iexact = key, variation_value__iexact = value)
                print('variation is ', variation)
            except:
                pass
    try:
        cart = Cart.objects.get(cartid=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cartid=_cart_id(request))
    cart.save()

    try:
        cart_item = CartItem.objects.get(cart=cart,product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product,cart=cart,quantity=1)
        cart_item.save()
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cartid=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

def delete_cart_item(request,product_id):
    cart = Cart.objects.get(cartid=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item = CartItem.objects.get(cart=cart,product=product)
    cart_item.delete()
    return redirect('cart')

def cart(request,quantity=0,total=0,tax=0,grand_total=0,cart_items=None):
    try:
        cart = Cart.objects.get(cartid=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            quantity += cart_item.quantity
            total += (cart_item.quantity * cart_item.product.price)
        tax = (total * 2)/100
        grand_total = total + tax
    except Cart.DoesNotExist:
        pass
    context = {'quantity':quantity,'total':total,'cart_items':cart_items,'grand_total':grand_total,'tax':tax}
    return render(request,'store/cart.html',context)
