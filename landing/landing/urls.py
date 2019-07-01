from django.contrib import admin
from django.urls import path, re_path, include


admin.autodiscover()

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^', include('app.home.urls')),
]
