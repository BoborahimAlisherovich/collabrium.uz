from django.contrib import admin
from .models import Space, Faq,OurTeam,Rezident,Blog,Jihoz,Tarif,Plansedescription
from django.utils.html import format_html




# Re-register models in a custom order
class CollabriumAdminSite(admin.AdminSite):
    site_title = "Collabrium Admin"
    site_header = "Collabrium Administration"
    index_title = "Collabrium Modules"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        for app in app_list:
            if app['name'] == 'Collabrium':  
                app['models'].sort(key=lambda x: [
                    "Зона", "Услуга","Часто задаваемые вопросы", "Наша команда", "Резидент",   "Блог"
                ].index(x['name']))
        return app_list

admin_site = CollabriumAdminSite(name='collabrium')



def img(self, obj):
    if obj.image:  
        return format_html('<img width="100" height="100" src="{}" />'.format(obj.image.url))
    return "No Image"


class TarifInline(admin.TabularInline):  
    model = Tarif 
    fields = ("name","name_uz","name_en","name_ru", "duration","duration_uz","duration_en","duration_ru", "price")
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
    list_display = ('id', 'title', 'page_slug', 'get_space')
    search_fields = ('title', 'page_slug', 'space__space')  
    readonly_fields = ('page_slug',)

    def get_space(self, obj):
        return obj.space.space if obj.space else "No Space"
    get_space.short_description = 'Space'


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



@admin.register(Plansedescription)
class PlansedescriptionAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
