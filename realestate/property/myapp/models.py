from django.db import models
from datetime import datetime


# Create your models here.
class Property(models.Model):
    bedroom_choice = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
    )
    bathroom_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    retailer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    code = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.CharField(max_length=1, choices=bedroom_choice)
    bathrooms = models.CharField(max_length=1, choices=bedroom_choice)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.IntegerField()
    photo_main = models.ImageField(upload_to="product_images")
    photo_1 = models.ImageField(blank=True)
    photo_2 = models.ImageField(blank=True)
    photo_3 = models.ImageField(blank=True)
    photo_4 = models.ImageField(blank=True)
    photo_5 = models.ImageField(blank=True)
    photo_6 = models.ImageField(blank=True)
    photo_7 = models.ImageField(blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=250)


