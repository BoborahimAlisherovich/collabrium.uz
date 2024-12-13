from django.contrib import admin
from .models import Space, Faq,OurTeam,Rezident,Blog

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
class RezidentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'job', 'description', 'image')
    search_fields = ('name',)  

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'job', 'description', 'image') 
    search_fields = ('name',) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_cover', 'date')
    search_fields = ('title',)
    prepopulated_fields = {'page_slug': ('title',)}
