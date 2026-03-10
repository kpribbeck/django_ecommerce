from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name
    
    
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    size = models.IntegerField(max_digits=8)
    color = models.IntegerField(max_digits=8)
    sku = models.IntegerField(max_digits=12)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(max_digits=10)

    def __str__(self):
        return self.name
