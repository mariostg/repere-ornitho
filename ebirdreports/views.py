from django.shortcuts import render
from django.contrib import messages

from ebirdreports import reporter
import json

from geographie.models import Mrc


def index(request):
    return render(request, "ebirdreports/index.html")


def observation_last_seven_days(request, mrc_code: str):
    data = []
    mrc_code = mrc_code.upper()
    mrc_name = Mrc.objects.filter(code=mrc_code).first()
    if not mrc_name:
        messages.info(request, f"{mrc_code} non trouvé.")
    else:
        mrc_name = mrc_name.name
        data = reporter.observation_last_seven_days(mrc_code)
    return render(
        request,
        "ebirdreports/observation-last-seven-days.html",
        {"data": data, "mrc": mrc_name},
    )


def location_recent_observations(request, location):
    data = reporter.get_observations_location(location)
    return render(
        request,
        "ebirdreports/observation-last-seven-days.html",
        {"data": data, "mrc": location},
    )
