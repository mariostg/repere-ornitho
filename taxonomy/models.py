from django.db import models


class Taxonomy(models.Model):
    sciName = models.CharField("nom scientifique", max_length=75)
    comNameFr = models.CharField("nom français", max_length=75)
    comNameEs = models.CharField("nom espagnol", max_length=75)
    comNameEn = models.CharField("nom anglais", max_length=75)
    speciesCode = models.CharField("code d'espèce", max_length=75)
    category = models.CharField("catégorie", max_length=75)
    taxonOrder = models.CharField("taxon", max_length=75)
    bandingCodes = models.CharField("banding codes", max_length=75)
    comNameCodes = models.CharField("code commun", max_length=75)
    sciNameCodes = models.CharField("code scientifique", max_length=75)
    order = models.CharField("ordre", max_length=75)
    familyCode = models.CharField("code de famille", max_length=75)
    familyComName = models.CharField("nom de famille commun", max_length=75)
    familySciName = models.CharField("nom de famille scientifique", max_length=75)
    reportAs = models.CharField("rapport", max_length=75)
    extinct = models.CharField("éteint", max_length=75)
    extinctYear = models.CharField("année d'extinction", max_length=75)

    def __str__(self):
        return self.comNameFr

    class Meta:
        verbose_name_plural = "Taxonomie"
