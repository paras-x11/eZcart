from .models import Cart, CartItem

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