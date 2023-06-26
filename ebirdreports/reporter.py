from main.settings import API_KEY
from ebird.api import get_observations
from geographie.models import Mrc


def observation_last_seven_days(mrc_code):
    mrc = Mrc()
    mrc = mrc.code_is_good(mrc_code)
    if mrc == False:
        data = []
    else:
        data = get_observations(API_KEY, mrc.code, 7, locale="fr")
        data = sorted(data, key=lambda x: x["comName"])
    return data
