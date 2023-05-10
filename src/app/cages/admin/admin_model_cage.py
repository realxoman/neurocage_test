from django.contrib import admin
from cages.models import Cage

@admin.register(Cage)
class CageAdmin(admin.ModelAdmin):
    pass