from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    categoryDescription = models.CharField(max_length=50, null=True)
    categoryImage = models.ImageField(upload_to="category_images")

    def __str__(self):
        return self.categoryName
    

