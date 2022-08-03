from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'accounts'
urlpatterns = [

    path('', views.index, name="index"),
    path('register/',views.register, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('dashboard/',views.dashboard, name="dashboard"),
]