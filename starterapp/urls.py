from django.contrib import admin
from django.urls import path
from shared_app.api import api as shared_api
from tenant_app.api import api as tenant_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/shared/', shared_api.urls),
    path('api/tenant/', tenant_api.urls),
] 