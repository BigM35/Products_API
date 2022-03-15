from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    inventory_quantity = models.IntegerField()
    picture = models.ImageField(upload_to=None, height_field=5, width_field=5, max_length=100)