
from django.contrib import admin
from django.urls import path, include

import authentication
from .views import index, test_url, login_user, about, contacts

urlpatterns = [
    path('', include('authentication.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('test/', login_user),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]
