"""
Import in the taxonomy model the data read from the location indicated in the code.
Taxonomy model has its data deleted beforehand.
csv file must have header that match the model.
"""

from taxonomy.models import Taxonomy
import csv

with open("../repere-ornitho-data/taxonomy.csv") as f:
    reader = csv.reader(f)
    header = next(reader)  # pass the header

    Taxonomy.objects.all().delete()

    for row in reader:
        d = dict(zip(header, row))
        t = Taxonomy.objects.create(**d)
