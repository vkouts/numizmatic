from django.contrib import admin
from coin.models import Coin, CoinImage, CoinLink, CoinMaterial


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinImage)
class CoinImageAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinLink)
class CoinLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(CoinMaterial)
class CoinMaterialAdmin(admin.ModelAdmin):
    pass