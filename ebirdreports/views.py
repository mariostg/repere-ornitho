from django.shortcuts import render
from ebird.api import get_observations
from main.settings import API_KEY
import json

from geographie.models import Mrc


def index(request):
    return render(request, "ebirdreports/index.html")


def observation_municipalite(request, mrc_code, back):
    mrc = Mrc()
    mrc = mrc.code_is_good(mrc_code)
    if mrc == False:
        data = []
    else:
        data = get_observations(API_KEY, mrc.code, back, locale="fr")
        data = sorted(data, key=lambda x: x["comName"])

    return render(
        request,
        "ebirdreports/observation-municipalite.html",
        {"data": data, "mrc": mrc.name, "back": back},
    )
