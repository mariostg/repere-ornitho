from django.shortcuts import render
from sites.models import Site, Municipalite


def sites_favoris(request):
    data = Site.objects.all()
    munic = Municipalite.objects.all()
    return render(request, "sites/favoris.html", context={"data": data, "munic": munic})
