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
    list_display = ('id','name', 'job', 'description', 'image')  # Rezident modeli ustunlari
    search_fields = ('name',)  # Tuple shaklida

@admin.register(OurTeam)
class OurTeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'job', 'description', 'image')  # OurTeam modeli ustunlari
    search_fields = ('name',)  # Tuple shaklida

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_cover', 'date')  # `job` o'chirildi, chunki u Blog modelida mavjud emas
    search_fields = ('title',)  # Tuple shaklida
    prepopulated_fields = {'page_slug': ('title',)}  # To'g'ri maydon nomi
