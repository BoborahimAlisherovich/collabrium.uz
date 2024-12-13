from django.db import models

#1
class Space(models.Model):
    space = models.CharField(max_length=300)
    page_slug = models.SlugField(unique=True) 
    image = models.ImageField()

    def __str__(self):
        return f"{self.space}"
    

#2
class Faq(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    page_slug = models.SlugField()
    
    def __str__(self):
        return f"{self.title}"
    
    
#3
class Blog(models.Model):
    image_cover = models.ImageField(upload_to='Blog_images')
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    page_slug = models.SlugField()
    def __str__(self):
        return f"{self.title}"

#4
class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='OurTeam_images')
    job = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"


#5
class Rezident(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='rezident_images')
    job = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"



