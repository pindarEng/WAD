from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    class ProductType(models.TextChoices):
        HARDWARE = 'HW','Hardware'
        SOFTWARE = 'SW','Software'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=2,choices=ProductType.choices)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name
    