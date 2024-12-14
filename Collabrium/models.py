from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save,pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver


class Space(models.Model):
    space = models.CharField(max_length=300, verbose_name="места")
    page_slug = models.SlugField(unique=True, verbose_name="Слаг страницы")
    image = models.ImageField(upload_to='Images/space', verbose_name="изображение")
    is_potkast = models.BooleanField(default=False, verbose_name="Это подкаст")

    def __str__(self):
        return self.space

    class Meta:
        verbose_name = _("Место")
        verbose_name_plural = _("Места")


    
#2
class Faq(models.Model):
    title = models.CharField(max_length=300, verbose_name="Титул")
    text = models.TextField(verbose_name="Текст")
    page_slug = models.SlugField(verbose_name="Слаг страницы")

    class Meta:
        verbose_name = _("Часто задаваемые вопросы")
        verbose_name_plural = _("Часто задаваемые вопросы")
    
    def __str__(self):
        return f"{self.title}"
    

#3
class Blog(models.Model):

    image_cover = models.ImageField(upload_to='blog_images', verbose_name="Обложка изображения")
    date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    page_slug = models.SlugField(unique=True, verbose_name="Слаг страницы")
    main_title = models.CharField(max_length=200, verbose_name="Основной заголовок")
    text_first = RichTextField(verbose_name="Текст 1")
    text_second = RichTextField(verbose_name="Текст 2")
    image_first = models.ImageField(upload_to='blog_images', blank=True, null=True, verbose_name="Первое изображение")
    image_second = models.ImageField(upload_to='blog_images', blank=True, null=True, verbose_name="Второе изображение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Блог")
        verbose_name_plural = _("Блог")

#4
class OurTeam(models.Model):
    name = models.CharField(max_length=200,verbose_name="Имя")
    image = models.ImageField(upload_to='OurTeam_images',verbose_name="изображение")
    job = models.CharField(max_length=200,verbose_name="Работа")
    description = models.TextField(verbose_name="описание")
    class Meta:
        verbose_name = _("Наша команда")
        verbose_name_plural = _("Наша команда")

    def __str__(self):
        return f"{self.name}"


#5
class Rezident(models.Model):
    name = models.CharField(max_length=200,verbose_name="Имя")
    image = models.ImageField(upload_to='rezident_images',verbose_name="изображение")
    job = models.CharField(max_length=200,verbose_name="Работа")
    description = models.TextField(verbose_name="описание")
    class Meta:
        verbose_name = _("Резидент")
        verbose_name_plural = _("Резидент")

    def __str__(self):
        return f"{self.name}"


class Podkast(models.Model):
    total = models.CharField(max_length=200, verbose_name="инструмент")
    image = models.ImageField(upload_to="Images/podkast", verbose_name="изображение")

    def __str__(self):
        return self.total

    class Meta:
        verbose_name = _("Подкаст")
        verbose_name_plural = _("Подкасты")

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Space, Podkast

@receiver(pre_save, sender=Space)
def save_to_podkast_instead_of_space(sender, instance, **kwargs):
    """
    Agar is_potkast belgilangan bo'lsa:
    1. Podkast modeliga ma'lumot saqlanadi.
    2. Space modelini saqlash to'xtatiladi.
    """
    if instance.is_potkast:  # is_potkast True bo'lsa
        # Podkast obyektini yaratamiz yoki mavjud bo'lsa qaytaramiz
        Podkast.objects.get_or_create(
            total=instance.space,
            image=instance.image
        )
        # Space saqlanishini to'xtatamiz
