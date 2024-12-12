from django.contrib import admin

# Register your models here.
from .models import Rezident


@admin.register(Rezident)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'description', 'image')
    