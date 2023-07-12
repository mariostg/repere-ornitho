from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("geographie/", include("geographie.urls")),
    path("home/", include("home.urls")),
    path("sites/", include("sites.urls")),
    path("taxonomy/", include("taxonomy.urls")),
    path("report/", include("ebirdreports.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
