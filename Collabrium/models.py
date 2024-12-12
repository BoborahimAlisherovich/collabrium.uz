from django.db import models

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



