import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import timedelta

from .forms import LoginForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def test_url(request):
    info = request.META['CSRF_COOKIE']
    return HttpResponse(info)


def login_user1(request):
    context = {'login_form': LoginForm()}
    return render(request, 'test.html', context)


def login_user(request):
    date = request.GET['lol']
    data = request.GET['name']
    return HttpResponse(request, data)
