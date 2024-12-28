from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from unidecode import unidecode

class Blog(models.Model):
    image_cover = models.ImageField(upload_to='Images/blog_images', verbose_name="Обложка изображения")
    date = models.DateField(auto_now_add=False, verbose_name="Дата публикации")
    title = models.CharField(max_length=255, verbose_name="Заголовок статьи")
    page_slug = models.SlugField(unique=True, blank=True, editable=False, verbose_name="Слаг страницы")
    main_title = models.CharField(max_length=200, verbose_name="Основной заголовок")
    text_first = RichTextField(verbose_name="Текст 1")
    text_second = RichTextField(verbose_name="Текст 2")
    image_first = models.ImageField(upload_to='Images/blog_images', blank=True, null=True, verbose_name="Первое изображение")
    image_second = models.ImageField(upload_to='Images/blog_images', blank=True, null=True, verbose_name="Второе изображение")

    
    def save(self, *args, **kwargs):
        self.page_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Блог ")
        verbose_name_plural = _("Блог ")

#4
class OurTeam(models.Model):
    name = models.CharField(max_length=200,verbose_name="Имя")
    image = models.ImageField(upload_to='Images/OurTeam_images',verbose_name="изображение")
    job = models.CharField(max_length=200,verbose_name="Работа")
    description = models.TextField(verbose_name="описание")
    class Meta:
        verbose_name = _("Наша команда ")
        verbose_name_plural = _("Наша команда ")

    def __str__(self):
        return f"{self.name}"


#5
class Rezident(models.Model):
    name = models.CharField(max_length=200,verbose_name="Имя")
    image = models.ImageField(upload_to='Images/rezident_images',verbose_name="изображение")
    job = models.CharField(max_length=200,verbose_name="Работа")
    description = models.TextField(verbose_name="описание")
    class Meta:
        verbose_name = _("Резидент ")
        verbose_name_plural = _("Резидент ")

    def __str__(self):
        return f"{self.name}"

class Space(models.Model):
    space = models.CharField(max_length=300, verbose_name="зона")
    page_slug = models.SlugField(unique=True, blank=True, editable=False, verbose_name="Слаг страницы") 
    image = models.ImageField(upload_to='Images/space', verbose_name="изображение")

    def save(self, *args, **kwargs):
        self.page_slug = slugify(unidecode(self.space))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Зона ")
        verbose_name_plural = _("Зона ")
    
    def __str__(self):
        return self.space

class Tarif(models.Model):
    space = models.ForeignKey(Space, related_name='Определения', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="Имя")
    duration = models.CharField(max_length=50, help_text="Davomiylik, masalan: '1 oy', '3 oy', '1 yil'",blank=True,null=True,verbose_name="Продолжительность")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")

    class Meta:
        verbose_name = _("Определение ")
        verbose_name_plural = _("Определения ")
    def __str__(self):
        return f"{self.name}"


class Plansedescription(models.Model):
    description = models.CharField(max_length=200,verbose_name="текст")
    plans = models.ManyToManyField(
        "Collabrium.Tarif",
        related_name="Plansedescriptions",verbose_name="подписка")
    
    def __str__(self):
        return f"{self.description}"
    
    class Meta:
        verbose_name = _("Услуга ")
        verbose_name_plural = _("Услуга ")

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
        verbose_name = _("Подкаст ")
        verbose_name_plural = _("Подкасты ")

class Faq(models.Model):
    title = models.CharField(max_length=300, verbose_name="Заголовок")
    text = RichTextField(verbose_name="Текст")
    page_slug = models.SlugField(unique=True, blank=True, editable=False, verbose_name="Слаг страницы")
    space = models.ForeignKey(Space, on_delete=models.CASCADE, verbose_name="Зона", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.space:
            self.space, _ = Space.objects.get_or_create(space="home", defaults={"page_slug": "home"})
        if not self.page_slug:
            self.page_slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    @property
    def space_name(self):
        return self.space.space

    class Meta:
        verbose_name = _("Вопросы ")
        verbose_name_plural = _("Вопросы ")

    def __str__(self):
        return self.title