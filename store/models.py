from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Brand(models.Model):
    brand_id = models.IntegerField(auto_created=True, null=True, blank=True)
    brand_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True) 

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=200, null=True)
    detail = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
