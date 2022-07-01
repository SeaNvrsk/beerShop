import apps.authentication
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from apps.core.views import index, about, contacts, userSettings, test, productListView, productItem


urlpatterns = [
    path('', include('apps.authentication.urls')),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('usersettings/', userSettings, name='usersettings'),
    path('list/', productListView, name='list'),
    path('list/<str:slug>', productItem, name='product'),
    re_path(r'\d\d/\d\d', test),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
