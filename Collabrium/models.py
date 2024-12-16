from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from unidecode import unidecode

#2
class Faq(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок")
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
    date = models.DateField(auto_now_add=False, verbose_name="Дата публикации")
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

class Space(models.Model):
    space = models.CharField(max_length=300, verbose_name="зоны")
    page_slug = models.SlugField(unique=True, blank=True, verbose_name="Слаг страницы",editable=False) 
    image = models.ImageField(upload_to='Images/space', verbose_name="изображение")

    def save(self, *args, **kwargs):
        self.page_slug = slugify(unidecode(self.space))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Зоны")
        verbose_name_plural = _("Зоны")


class Jihoz(models.Model):
    space = models.ForeignKey(
        Space, 
        on_delete=models.CASCADE, 
        related_name="jihozlar", 
        verbose_name="Связанное пространство"
    )
    total = models.CharField(max_length=200, verbose_name="инструмент")
    image = models.ImageField(upload_to="Images/podkast", verbose_name="изображение")

    def __str__(self):
        return self.total

    class Meta:
        verbose_name = _("Подкаст")
        verbose_name_plural = _("Подкасты")


