from django.urls import path
from . import views

urlpatterns = [
    path("site-favoris", views.sites_favoris, name="sites-favoris"),
]
