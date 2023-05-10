from django.contrib import admin
from cages.models import CageAnalytical

@admin.register(CageAnalytical)
class CageAnalyticalAdmin(admin.ModelAdmin):
    pass