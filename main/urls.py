
from django.contrib import admin
from django.urls import path, include

import authentication
from .views import index, about, contacts, userSettings

urlpatterns = [
    path('', include('authentication.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('usersettings/', userSettings, name='usersettings')
]
