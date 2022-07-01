import datetime

from django.shortcuts import render
from django.contrib.auth.admin import User
from django.http import HttpResponse, HttpRequest
from datetime import timedelta
from apps.user.models import UserProfile
from apps.shop.models import Product, Comments, CommentsForm
from django.shortcuts import redirect

from .forms import LoginForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def userSettings(request):
    userInfo = UserProfile.objects.get(user=request.user)
    return render(request, 'usersettings.html', {'userInfo': userInfo})


def test(request):
    return HttpResponse('test')


def productListView(request):
    content = Product.objects.all()
    return render(request, 'list.html', {'content': content})


def productItem(request, slug):
    product = Product.objects.get(slug=slug)
    comments = Comments.objects.filter(product=product)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.name = request.user
            comment.product = product
            comment.save()
            return render(request, 'product.html', {'cont': product, 'form': form, 'comments': comments})
    else:
        form = CommentsForm()
    return render(request, 'product.html', {'cont': product, 'form': form, 'comments': comments})



