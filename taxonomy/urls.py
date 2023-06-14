from django.urls import path
from . import views

urlpatterns = [
    path("search", views.search_species, name="search-species"),
    path("order/<str:order>/", views.order, name="order"),
    path("famille_sci/<str:familySciName>/", views.famille_sci, name="family-sci-name"),
]
