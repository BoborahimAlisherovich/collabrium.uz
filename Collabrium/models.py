from django.db import models

#1
from django.utils.translation import gettext_lazy as _

class Space(models.Model):
    space = models.CharField(max_length=300)
    page_slug = models.SlugField(unique=True) 
    image = models.ImageField(upload_to='Images/space')
    class Meta:
        verbose_name = _("пространства")
        verbose_name_plural = _("пространства")

    def __str__(self):
        return f"{self.space}"
    

#2
class Faq(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    page_slug = models.SlugField()

    class Meta:
        verbose_name = _("Часто задаваемые вопросы")
        verbose_name_plural = _("Часто задаваемые вопросыc")
    
    def __str__(self):
        return f"{self.title}"
    

#3
class Blog(models.Model):
    image_cover = models.ImageField(upload_to='Blog_images',verbose_name="Обложка изображения")
    date = models.DateField(auto_now_add=True,verbose_name="Дата публикации")
    title = models.CharField(max_length=255,verbose_name="Заголовок статьи")
    page_slug = models.SlugField(unique=True,verbose_name="Слаг страницы")

    def __str__(self):
        return f"{self.title}"
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
        verbose_name_plural = _("Наша командаc")

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
        verbose_name_plural = _("Резидентc")

    def __str__(self):
        return f"{self.name}"



