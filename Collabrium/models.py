from django.db import models
from django.utils.translation import gettext_lazy as _

class Space(models.Model):
    space = models.CharField(max_length=300)
    page_slug = models.SlugField(unique=True) 
    image = models.ImageField(upload_to='Images/space')
    class Meta:
        verbose_name = _("Space")
        verbose_name_plural = _("Spaces")

    def __str__(self):
        return f"{self.space}"
    

class Faq(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    page_slug = models.SlugField()
    class Meta:
        verbose_name = _("Faq")
        verbose_name_plural = _("Faqs")
    
    def __str__(self):
        return f"{self.title}"
    








class OurTeam(models.Model):
    name = models.TextField()
    image = models.ImageField()
    job = models.TextField()
    description = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Rezident(models.Model):
    name = models.TextField()
    image = models.ImageField()
    job = models.TextField()
    description = models.CharField(max_length = 1000)
    def __str__(self):
        return f"{self.name}"



