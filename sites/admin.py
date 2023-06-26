from django.contrib import admin
from .models import Site


class SiteAdmin(admin.ModelAdmin):
    list_display = ("site_name", "loc_id", "municipalite")


admin.site.register(Site, SiteAdmin)
