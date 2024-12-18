from modeltranslation.translator import register, TranslationOptions
from .models import Space, Faq, OurTeam, Rezident, Blog,Jihoz

@register(Space)
class NewsTranslationOptions(TranslationOptions):
    fields = ('space',) 

@register(Faq)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

@register(OurTeam)
class NewsTranslationOptions(TranslationOptions): 
    fields = ('name', 'description', 'job') 

@register(Rezident)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'job') 

@register(Blog)
class NewsTranslationOptions(TranslationOptions):  
    fields = ('title', 'main_title', 'text_first', 'text_second') 

@register(Jihoz)
class NewsTranslationOptions(TranslationOptions):  
    fields = ('total',)


