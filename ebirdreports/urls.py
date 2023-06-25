from django.urls import path
from ebirdreports import views

urlpatterns = [
    path("", views.index, name="report-index"),
    path("<str:municipalite>/<int:back>/", views.observation_municipalite, name="observation-municipalite"),
]
