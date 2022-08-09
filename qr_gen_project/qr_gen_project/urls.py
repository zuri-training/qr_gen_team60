# qr_gen_project/settings.py

from re import M
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="QR Planets API Documentation",
      default_version='v1',
      description="""The Easiest Way to generate, download &amp; share QR CodesOnline with QR Planet Code Generator within few minutes.
      Get started today.
      These are the Available Endpoints, Other API Endpoints are coming soon""",
      
      contact=openapi.Contact(email="simplenick01@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[]
)


urlpatterns = [
   path('qr-gen/api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('qr-gen/api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




urlpatterns += [
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