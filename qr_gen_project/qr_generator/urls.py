

from django.urls import path
from qr_generator import views


app_name = 'qr_generator'

urlpatterns = [
    # path('qr',views.qr_request, name='qr'),
    path('qr-page', views.QR_page, name='qr_page'),
]

urlpatterns += [
    path('text-qr/<str:text>/', views.text, name='text'),
    path('url-qr/<str:url>/', views.text, name='url'),
]


urlpatterns += [
    path('', views.index, name="home"),
    path('generate-qr/', views.generate_qr, name='generate_qr'),
    path('share-qr/<str:pk>/', views.share_qr, name='share'),
    path('download-qr/<str:id>/<str:file_type>/', views.download_file, name='download'),
    path('save-qr/<str:id>/', views.save_qr, name='save_qr'),
]

urlpatterns +=[
    # path("<int:qr_id>/", views.get_qr, name="get_qr"),
    path('contact-us/', views.contact_us, name='contact'),
]

urlpatterns += [
    path('learn-more/', views.learn_more, name="learn_more"), 
]