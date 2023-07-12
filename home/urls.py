from django.urls import path
import home.views
import ebirdreports.views

# from ebirdreports import views


urlpatterns = [
    path("", home.views.home, name="home"),
]
