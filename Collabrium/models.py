from django.db import models


class Space(models.Model):
    space = models.CharField(max_length=300)
    page_slug = models.SlugField(unique=True) 
    image = models.ImageField(upload_to='Images/space')

    def __str__(self):
        return f"{self.space}"
    

class Faq(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    page_slug = models.SlugField()
    
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



