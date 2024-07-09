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
    
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id}"
    
class OrderLineItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,related_name='lineItems',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.qty} of {self.product.name}"

