import datetime
import logging

from django.shortcuts import render
from django.contrib.auth.admin import User
from django.http import HttpResponse, HttpRequest
from datetime import timedelta

from apps.core.models import Product, Comment

from django.shortcuts import redirect
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
def test(request):
    return HttpResponse('test')






