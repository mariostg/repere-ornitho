from django.shortcuts import render
from sites.models import Site, Municipalite


def sites_favoris(request):
    grouped = dict()

    for obj in Site.objects.all():
        grouped.setdefault(obj.municipalite.name, []).append([obj.site_name, obj.loc_id])
    return render(request, "sites/favoris.html", context={"data": grouped})
