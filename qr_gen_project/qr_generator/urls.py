

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"), 
]

urlpatterns +=[
    path('test', views.qr_gen, name="home"),
]

<<<<<<< HEAD

urlpatterns +=[
    path('contact', views.contact_us, name='contact'),
]

urlpatterns +=[
    path('nick', views.qr_gen2, name="test"),
    path('<str:template>/', views.form, name='form'),
=======
urlpatterns +=[
    path('<str:template>/', views.test_form, name='form'),
>>>>>>> a84a2e4572177ea61c7c5789f04c087874aa5d86
]