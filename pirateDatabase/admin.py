from django.contrib import admin

from pirateDatabase.models import Pirate


@admin.register(Pirate)
class PirateAdmin(admin.ModelAdmin):
    pass
