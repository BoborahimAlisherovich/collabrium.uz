from django.contrib import admin
from .models import Space, Faq,OurTeam,Rezident,Blog,Jihoz,Tarif
from django.utils.html import format_html

def img(self, obj):
    if obj.image:  
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))
    return "No Image"


class TarifInline(admin.TabularInline):  # Changed from ModelAdmin to TabularInline
    model = Tarif 
    fields = ("name", "duration", "description", "price")
    verbose_name = "тариф"
    verbose_name_plural = "тариф"



class JihozInline(admin.TabularInline):
    model = Jihoz 
    fields = ("total","total_uz","total_ru","total_en", "image")
    verbose_name = "Инструмент"
    verbose_name_plural = "Инструмент"



@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('space', 'page_slug', 'image')
    search_fields = ('space', 'page_slug')

    readonly_fields = ('page_slug',)
    
    inlines = [JihozInline,TarifInline]
    

    fieldsets = (
        ("Основная информация", {
            "fields": ("space", "space_uz", "space_ru", "space_en", "image", "page_slug"),
        }),
    )


    def img(self, obj):
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('id', 'page_slug','title')
    search_fields = ('page_slug','title')
    readonly_fields = ('page_slug',)

    
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
    readonly_fields = ('page_slug',)
