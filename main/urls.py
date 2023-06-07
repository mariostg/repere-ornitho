from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("home/", include("home.urls")),
    path("taxonomy/", include("taxonomy.urls")),
]
