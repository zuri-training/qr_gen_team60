from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [

    path('', views.index, name="index"),
    path('register/',views.register, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout, name="logout"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('faq/', views.faq, name="faq"),
]