from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Movie(models.Model):
    film_adi = models.CharField(max_length=200)
    aciklama = models.TextField()
    image = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)