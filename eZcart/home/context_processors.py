from .models import *

def cart_count(request):
    cart_count = 0
    if request.user.is_authenticated:
        try:
            # Get the cart for the authenticated user
            cart = Cart.objects.get(user=request.user)
            
            # Count the unique items in the cart (i.e., CartItem instances)
            cart_count = cart.cart_items.count()
        except Cart.DoesNotExist:
            cart_count = 0
            
    return {'cart_count': cart_count}

def wishlist_count(request):
    wishlist_count = 0
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()
    return {'wishlist_count': wishlist_count}