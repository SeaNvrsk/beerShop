import apps.authentication
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.core.views import *
from apps.core.services.views import *


urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('cart/', include('apps.cart.urls', namespace='core')),
    path('', indexView),
    path('admin/', admin.site.urls),
    path('index/', indexView, name='index'),
    path('about/', aboutView, name='about'),
    path('contacts/', contactsView, name='contacts'),
    path('usersettings/', userSettingsView, name='usersettings'),
    path('list/', productListView, name='list'),
    path('list/<str:slug>', productItemView, name='product'),
    path('test/', testView),
    re_path(r'\d\d/\d\d', testView),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
