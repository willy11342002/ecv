from django.conf.urls import include
from django.contrib import admin
from django.urls import path
import apiV1

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'apiv1/', include('apiV1.urls')),
]
