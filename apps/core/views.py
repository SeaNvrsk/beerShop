import datetime
import logging

from django.shortcuts import render
from django.contrib.auth.admin import User
from django.http import HttpResponse, HttpRequest
from datetime import timedelta
from apps.cart.forms import CartAddProductForm

from apps.core.models import Product, Comment

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
# Create your views here.

logger = logging.getLogger('main')


def indexView(request):
    return render(request, 'core/index.html')


def aboutView(request):
    return render(request, 'about.html')


@login_required()
def contactsView(request):
    return render(request, 'contacts.html')


@login_required()
def testView(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'test.html', {'context': num_visits})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'core/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})







