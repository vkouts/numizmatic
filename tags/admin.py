from django.contrib import admin

from tags.models import CoinTags


@admin.register(CoinTags)
class CoinTagsAdmin(admin.ModelAdmin):
    pass
