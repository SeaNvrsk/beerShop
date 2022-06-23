import datetime

from django.shortcuts import render
from django.contrib.auth.admin import User
from django.http import HttpResponse, HttpRequest
from datetime import timedelta
from user.models import UserProfile

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
