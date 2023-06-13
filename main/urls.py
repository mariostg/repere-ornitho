from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("geographie/", include("geographie.urls")),
    path("home/", include("home.urls")),
    path("sites/", include("sites.urls")),
    path("taxonomy/", include("taxonomy.urls")),
]
