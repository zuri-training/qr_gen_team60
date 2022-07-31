from rest_framework import routers
from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:pk>/', views.qr_view),
]