import pandas as pd

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
