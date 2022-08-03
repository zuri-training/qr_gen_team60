

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"), 
]

urlpatterns +=[
    path('test', views.qr_gen, name="home"),
]

urlpatterns +=[
    path('<str:template>/', views.test_form, name='form'),
]