from modeltranslation.translator import register, TranslationOptions
from .models import Space,Faq,OurTeam,Rezident

@register(Space)
class SpaceTranslationOptions(TranslationOptions):
    fields = ('space',)

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('title','text')

@register(OurTeam)
class OurTramTranslationOptions(TranslationOptions):
    fields = ('name','description','job')

@register(Rezident)
class RezidentTranslationOptions(TranslationOptions):
    fields = ('name','description','job')


