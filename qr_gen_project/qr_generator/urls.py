

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'
urlpatterns = [
    path('', views.index, name="home"),
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('share-qr/<str:pk>/', views.share_qr, name='share'),
    path('download-qr/<str:filetype>/', views.download_file, name='download_qr'),
    path('save-qr/', views.save_qr, name='save_qr'),
]

urlpatterns +=[
    path("<int:qr_id>/", views.get_qr, name="get_qr"),
    path('contact-us/', views.contact_us, name='contact'),
]

urlpatterns += [
    path('learn-more/', views.learn_more, name="learn_more"), 
]