from taxonomy.models import Taxonomy


def search_species(request):
    search_term = ""
    query_string = ""
    data = Taxonomy.objects.all()
    query_terms = set()
    if request.GET.get("search_term"):
        search_term = request.GET.get("search_term")
        query_terms.add(f"search_term={search_term}")
        data = (
            data.filter(comNameFr__contains=search_term)
            | data.filter(comNameEn__contains=search_term)
            | data.filter(comNameEs__contains=search_term)
        )

    initial = {"search_term": search_term}
    if len(query_terms) > 0:
        query_string = "&".join(query_terms)

    print(data, initial, query_string)
    return data, initial, query_string
