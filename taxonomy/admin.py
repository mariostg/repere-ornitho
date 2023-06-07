from django.contrib import admin
from .models import Taxonomy


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ("comNameFr", "comNameEn", "comNameEs", "sciName")


admin.site.register(Taxonomy, TaxonomyAdmin)
