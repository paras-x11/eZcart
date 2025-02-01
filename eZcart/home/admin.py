from django.contrib import admin
from home.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName', 'categoryDescription', 'categoryImage')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'productName', 'productPrice', 'productQty', 'productImage')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)