from django.shortcuts import render
from ebird.api import get_observations
import environ
import json


def index(request):
    return render(request, "ebirdreports/index.html")


def observation_municipalite(request, municipalite, back):
    with open("ca-qc-ou.json", "r") as f:
        data = json.load(f)

    # env = environ.Env()
    # environ.Env.read_env()
    # API_KEY = env("API_KEY")

    # data = get_observations(API_KEY, municipalite, back)

    return render(
        request,
        "ebirdreports/observation-municipalite.html",
        {
            "data": data,
            "municipalite": municipalite,
            "back": back,
        },
    )
