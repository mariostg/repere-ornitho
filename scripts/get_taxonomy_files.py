from main.settings import API_KEY
import json
from ebird.api import get_taxonomy


en_taxonomy = get_taxonomy(API_KEY)
json_obj = json.dumps(en_taxonomy, indent=4)
with open("en_taxonomy.json", "w") as f:
    f.write(json_obj)

fr_taxonomy = get_taxonomy(API_KEY, locale="fr")
json_obj = json.dumps(fr_taxonomy, indent=4)
with open("fr_taxonomy.json", "w") as f:
    f.write(json_obj)

es_taxonomy = get_taxonomy(API_KEY, locale="es")
json_obj = json.dumps(es_taxonomy, indent=4)
with open("es_taxonomy.json", "w") as f:
    f.write(json_obj)
