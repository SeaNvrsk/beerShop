import logging

from django.shortcuts import render
from apps.user.models import UserProfile
from apps.core.models import *
from apps.core.forms import CommentForm
from apps.cart.forms import CartAddProductForm


logger = logging.getLogger('main')


def userSettingsView(request):
    logger.info('another Test')
    userInfo = UserProfile.objects.get(user=request.user)
    return render(request, 'usersettings.html', {'userInfo': userInfo})


def productListView(request):
    logger.info('TEST')
    content = Product.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'list.html', {'content': content, 'cart_product_form': cart_product_form})


def productItemView(request, slug):
    product = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product=product)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user
            comment.product = product
            comment.save()
    form = CommentForm()
    return render(request, 'product.html', {'cont': product, 'form': form, 'comments': comments})
