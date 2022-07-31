
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import include, re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
