from django.contrib import admin
from django.utils.html import format_html  # for Image field 
from home.models import *

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName', 'categoryDescription', 'get_image')
    search_fields = ('categoryName',)

    def get_image(self, obj):
        if obj.categoryImage:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.categoryImage.url))
        return "No Image"
    
    get_image.short_description = "Category Image"


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'productName', 'productPrice', 'productQty', 'get_image')
    list_filter = ('category',)
    search_fields = ('productName',)

    def get_image(self, obj):
        if obj.productImage:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.productImage.url))
        return "No Image"

    get_image.short_description = "Product Image"


# Cart Admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'total_cart_price')
    search_fields = ('user__username',)


# CartItem Admin
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'qty', 'total_price')
    search_fields = ('cart__user__username', 'product__productName')


# ✅ Register models in admin panel
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
