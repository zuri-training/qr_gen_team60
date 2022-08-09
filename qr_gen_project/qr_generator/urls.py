

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"), 
    path('contact-us/', views.contact_us, name='contact'),
    path('generator/', views.generate, name='generator')
]