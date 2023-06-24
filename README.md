The Ebird.api module is included here because the one from pip install ebird-api is broken. It does not allow languages other than English.

There must be a .env file at the same level as manage.py
It must contain the key pair value of the API key:
API_KEY='xxxxxxxx'

## Setting up the taxonomy table

```
python scripts/get_taxonomy_files.py
python scripts/merge_taxonomy.py
python manage.py runscript scripts.import-taxonomy
```
