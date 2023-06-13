from django.shortcuts import render
from sites.models import Site


def sites_favoris(request):
    data = Site.objects.all()
    print(data)
    return render(request, "sites/favoris.html", context={"data": data})
