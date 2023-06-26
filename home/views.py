from django.shortcuts import render
from geographie.models import Mrc


def home(request):
    mrc = Mrc.objects.all()
    context = {"mrc": mrc}
    return render(request, "home/home.html", context)
