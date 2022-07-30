
from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name ='signup'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]
