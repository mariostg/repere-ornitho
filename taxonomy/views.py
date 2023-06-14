from django.shortcuts import render
from django.core.paginator import Paginator
from taxonomy.forms import SearchSpeciesForm
from utils import search
from taxonomy.models import Taxonomy


def search_species(request):
    species, initial, query_string = search.search_species(request)
    paginator = Paginator(species, 25)
    page_number = request.GET.get("page")
    form = SearchSpeciesForm(initial=initial)
    context = {
        "data": paginator.get_page(page_number),
        "form": form,
        "initial": initial,
        "query_string": query_string,
    }
    return render(request, "taxonomy/search-page.html", context)


def order(request, order):
    data = Taxonomy.objects.all().filter(order=order)
    paginator = Paginator(data, 25)
    page_number = request.GET.get("page")
    context = {
        "data": paginator.get_page(page_number),
    }
    return render(request, "taxonomy/search-page.html", context)


def famille_sci(request, familySciName):
    data = Taxonomy.objects.all().filter(familySciName=familySciName)
    paginator = Paginator(data, 25)
    page_number = request.GET.get("page")
    context = {
        "data": paginator.get_page(page_number),
    }
    return render(request, "taxonomy/search-page.html", context)
