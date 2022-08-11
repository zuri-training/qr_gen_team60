

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"), 
]

urlpatterns +=[
    path('test', views.qr_gen, name="home"),
    path("<int:qr_id>/", views.get_qr, name="get_qr")
    path('contact-us/', views.contact_us, name='contact'),
    path('generator/<str:extra_args>', views.generate, name='generator')
]

urlpatterns += [
    path('learn-more/', views.learn_more, name="learn_more"), 
]