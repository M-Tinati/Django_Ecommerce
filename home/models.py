from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12 , decimal_places=0)
    img = models.ImageField(upload_to='picture/')
