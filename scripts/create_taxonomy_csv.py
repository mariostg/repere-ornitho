from main.settings import API_KEY
import pandas as pd
import json
from ebird.api import get_taxonomy


def write_taxonomy_files():
    print(API_KEY)
    return
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


def merge_tanonomy():
    en_taxonomy = pd.read_json("en_taxonomy.json")
    en_taxonomy = en_taxonomy.rename(columns={"comName": "comNameEn"})

    fr_taxonomy = pd.read_json("fr_taxonomy.json")
    fr_taxonomy = fr_taxonomy.rename(columns={"comName": "comNameFr"})

    es_taxonomy = pd.read_json("es_taxonomy.json")
    es_taxonomy = es_taxonomy.rename(columns={"comName": "comNameEs"})

    merged = pd.merge(en_taxonomy, fr_taxonomy[["sciName", "comNameFr"]], on="sciName")
    merged = pd.merge(merged, es_taxonomy[["sciName", "comNameEs"]], on="sciName")

    cols = list(merged.columns)
    cols.insert(1, cols.pop())
    cols.insert(1, cols.pop())
    merged = merged.reindex(columns=cols)

    merged.to_csv("taxonomy.csv", index=False)


write_taxonomy_files()
