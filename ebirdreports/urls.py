from django.urls import path
from ebirdreports import views

urlpatterns = [
    path("", views.index, name="report-index"),
    path("<str:mrc_code>/", views.observation_last_seven_days, name="last-seven-days"),
]
