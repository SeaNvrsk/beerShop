
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
