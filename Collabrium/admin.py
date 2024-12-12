from django.contrib import admin
from .models import Rezident
from .models import Space, Faq

@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'space', 'page_slug', 'image')
    search_fields = ('space', 'page_slug')
    prepopulated_fields = {'page_slug': ('space',)}


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page_slug')
    search_fields = ('title', 'page_slug')
    prepopulated_fields = {'page_slug': ('title',)}




    

@admin.register(Rezident)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'description', 'image')
    