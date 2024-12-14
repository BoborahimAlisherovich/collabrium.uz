from modeltranslation.translator import register, TranslationOptions
from .models import Space, Faq, OurTeam, Rezident, Blog,Podkast

@register(Space)
class SpaceTranslationOptions(TranslationOptions):
    fields = ('space',) 

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

@register(OurTeam)
class OurTeamTranslationOptions(TranslationOptions): 
    fields = ('name', 'description', 'job') 

@register(Rezident)
class RezidentTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'job') 

@register(Blog)
class BlogTranslationOptions(TranslationOptions):  
    fields = ('title', 'main_title', 'text_first', 'text_second') 

@register(Podkast)
class PodkastranslationOptions(TranslationOptions):  
    fields = ('totel',)
