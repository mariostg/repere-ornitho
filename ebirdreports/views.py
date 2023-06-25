from django.shortcuts import render
from ebird.api import get_observations
import environ
import json

from geographie.models import Mrc


def index(request):
    return render(request, "ebirdreports/index.html")


def observation_municipalite(request, mrc_code, back):
    with open("ca-qc-ou.json", "r") as f:
        data = json.load(f)

    # env = environ.Env()
    # environ.Env.read_env()
    # API_KEY = env("API_KEY")

    # data = get_observations(API_KEY, mrc, back)

    mrc = Mrc()
    mrc = mrc.code_is_good(mrc_code)
    if mrc == False:
        data = []
    return render(
        request,
        "ebirdreports/observation-municipalite.html",
        {"data": data, "mrc": mrc, "back": back},
    )
