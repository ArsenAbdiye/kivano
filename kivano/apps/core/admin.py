from django.contrib import admin
from .models import *


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    pass


@admin.register(PlatformLink)
class PlatformLinkkAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass