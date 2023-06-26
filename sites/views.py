from django.shortcuts import render
from sites.models import Site, Municipalite


def sites_favoris(request):
    return render(request, "sites/favoris.html", context={"sites": Site.objects.all()})
