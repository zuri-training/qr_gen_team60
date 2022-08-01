from rest_framework import routers
from django.urls import include, path
from . import views


urlpatterns = [
    path('<str:pk>/category/<str:category>/<str:item>/', views.get_one_qr), # Fetch one QR from a category, #!not yet working properly
    path('<str:pk>/category/<str:category>/', views.get_qr_from_category), # fetch all QR from a category,
    path('<str:pk>/', views.get_all_user_qr), # Fetch all user QR codes
    path('<str:pk>/category/<str:category>create/', views.send_qr), # Create a new qr_code from URL #!not yet working properly
]

urlpatterns +=[
    path('<str:pk>/category/<str:item>/delete',views.delete_one_qr), # delete one qr from a category #!not yet working properly
    #path('<int:pk>/category/delete',views.delete_one_qr), # delete one category,
    #path('<int:pk>/delete', views.delete_all),
    #path('<int:pk>/category/update', views.update)
]