from modeltranslation.translator import register, TranslationOptions
from .models import Space,Faq

@register(Space)
class SpaceTranslationOptions(TranslationOptions):
    fields = ('space',)

@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('title','text')