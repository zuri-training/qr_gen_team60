

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
    path('contact', views.contact_us, name='contact'),
]

urlpatterns +=[
    path('nick', views.qr_gen2, name="test"),
    path('<str:template>/', views.form, name='form'),
]