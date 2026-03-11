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
    size = models.IntegerField()
    color = models.IntegerField()
    sku = models.IntegerField()
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
