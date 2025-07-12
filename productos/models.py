from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    description = models.TextField()
    image = models.ImageField(null=True,blank=True,upload_to='products/') 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.TimeField(default=timezone.now())
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="products", null=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.sku} {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments",null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments",null=True)
    comment = models.TextField()
    created_at = models.TimeField(default=timezone.now)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"