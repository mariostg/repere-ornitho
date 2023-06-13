from django.shortcuts import render


def sites_favoris(request):
    return render(request, "sites/favoris.html")
