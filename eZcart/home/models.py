from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    categoryDescription = models.CharField(max_length=50, null=True)
    categoryImage = models.ImageField(upload_to="category_images")

    def __str__(self):
        return self.categoryName
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productQty = models.IntegerField(null=False, blank=False, default=10, validators=[MinValueValidator(0), MaxValueValidator(1000)], help_text="Stock quantity must be between 0 and 1000.")
    productImage = models.ImageField(upload_to="product_images")

    def __str__(self):
        return self.productName
    


