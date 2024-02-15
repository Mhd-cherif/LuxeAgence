from django.contrib import admin
from .models import Residence

# Register your models here.

@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'nomResidence', 'description')