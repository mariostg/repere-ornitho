from django.db import models

# Create your models here.
class Site(models.Model):
    site_name = models.CharField("Nom du site", max_length=75)
    loc_id = models.CharField("Id de localisation", max_length=10)
