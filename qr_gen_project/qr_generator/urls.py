

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"), 
]

urlpatterns +=[
    path('test', views.qr_gen, name="home"),
    path("<int:qr_id>/", views.get_qr, name="get_qr")
]