# qr_gen_project/settings.py

from re import M
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('qr-gen/', include('qr_generator.urls', namespace='qr_generator'),),
    path('qr-gen/admin/', admin.site.urls),
]

urlpatterns += [
    path('qr-gen/accounts/', include('accounts.urls', namespace='accounts'),),
]

urlpatterns += [
    path('qr-gen/api/', include('api.urls'), ),
]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)