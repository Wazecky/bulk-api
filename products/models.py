from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('images', filename)

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')

    def __str__(self):
        return f"{self.product.name} - {self.name}"
