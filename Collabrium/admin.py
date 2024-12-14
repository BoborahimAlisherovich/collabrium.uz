from django.contrib import admin
from .models import Space, Faq,OurTeam,Rezident,Blog,Podkast
from django.utils.html import format_html

def img(self, obj):
    if obj.image:  # Rasm mavjudligini tekshirish
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))
    return "No Image"


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'space', 'page_slug','img')
    search_fields = ('space', 'page_slug')
    prepopulated_fields = {'page_slug': ('space',)}
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page_slug')
    search_fields = ('title', 'page_slug')
    prepopulated_fields = {'page_slug': ('title',)}

@admin.register(Rezident)
class RezidentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'job', 'description','img')
    search_fields = ('name',)  
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'job', 'description','img') 
    search_fields = ('name',) 
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_cover', 'date')
    search_fields = ('title',)
    prepopulated_fields = {'page_slug': ('title',)}

@admin.register(Podkast)
class PodkastAdmin(admin.ModelAdmin):
    list_display = ('id','total', 'img')
    search_fields = ('total',)
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))
   

    
