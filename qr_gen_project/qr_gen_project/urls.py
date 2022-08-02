# qr_gen_project/settings.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# qr-gen/

urlpatterns = [
    path('', include('accounts.urls')),
]

urlpatterns += [
    path('qr-gen/', include('qr_generator.urls',), ),
    path('qr-gen/admin/', admin.site.urls),
    path('qr-gen/api/', include('api.urls'), ),
]



if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)