from django.contrib import admin
from mycoin.models import MyCoin, MyCoinImage


@admin.register(MyCoin)
class MyCoinAdmin(admin.ModelAdmin):
    pass


@admin.register(MyCoinImage)
class MyCoinImageAdmin(admin.ModelAdmin):
    pass
