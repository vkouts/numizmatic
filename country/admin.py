from django.contrib import admin
from country.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
