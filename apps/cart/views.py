from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from apps.core.models import Product
from apps.cart.cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    print(product, product_id, form)
    if form.is_valid():
        print(product)
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else:
        print('not working')
    print(form.errors)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, './cart/detail.html', {'cart': cart})


