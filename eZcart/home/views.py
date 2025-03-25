from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.models import *
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import razorpay

# Create your views here. 


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'is_index': True,  # Flag for index page
        'categories': categories,
        'products': products,
    }
    return render(request, "index.html", context)

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "shop.html", context)

def get_products_by_category(request):
    cid = request.GET.get("cid")
    if cid == "":
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=cid)

    product_list = [
        {
            'productId' : product.id,
            'productName': product.productName,
            'productPrice': product.productPrice,
            'productImage': { 'url': product.productImage.url }
        }
        for product in products
    ]
    return JsonResponse({"cproducts": product_list})

def searchProduct(request):
    val = request.GET.get('val')

    products = Product.objects.filter(productName__istartswith=val)

    product_list = [
        {
            'productId' : product.id,
            'productName': product.productName,
            'productPrice': product.productPrice,
            'productImage': { 'url': product.productImage.url }
        }
        for product in products
    ]
    return JsonResponse({"cproducts": product_list})

def product_detail(request):
    id = request.GET['id']
    pdata = Product.objects.get(pk=id)

    products = Product.objects.all()
    categories = Category.objects.all()

    context = {
        'pdata' : pdata,
        'categories': categories,
        'products': products,
    }
    return render(request, "product-detail.html", context)



def addToCart(request):
    pid = request.GET.get('pid') 
    qty = int( request.GET.get('qty') )
    user_id = request.user.id if request.user.is_authenticated else None
    
    if not pid:
        return JsonResponse({"error": "Product ID is required"}, status=400)

    print(pid, user_id, qty)
    try:
        user = request.user 
        product = Product.objects.get(pk=pid)

        # Get the user's cart, or create a new one if it doesn't exist
        cart, created = Cart.objects.get_or_create(user=user)
        
        # Check if the product is already in the cart
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        
        if cart_item:
            # Update the quantity if the product is already in the cart
            cart_item.qty += qty
            cart_item.save()
        else:
            # Create a new cart item if not already in the cart
            CartItem.objects.create(cart=cart, product=product, qty=qty)
            
        return JsonResponse({"success": True, "message": "Product added to cart"})
    
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)

def remove_from_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        try:
            cart_item = CartItem.objects.get(product__id=product_id, cart__user=request.user)  # User ka check lagana zaroori hai
            cart_item.delete()
            return JsonResponse({"status": "success"})
        except CartItem.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Item not found"})
    
    return JsonResponse({"status": "error", "message": "Invalid request"})

@login_required(login_url="login_user")
def shoping_cart(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)
    
    # Fetch cart items, it may be empty
    cart_items = CartItem.objects.filter(cart=cart)

    total = 0

    if not cart_items.exists():  
        cart_items = [] 
        total = 0
    else:
        for item in cart_items:  
            total += item.sub_total()  

    context = {
        'cart_items': cart_items,
        'total': total,
        'is_empty': not bool(cart_items),  
    }

    return render(request, "shoping-cart.html", context)

    

def changeQty(request):
    data = request.GET
    qty = int(data.get("qty"))
    cid = int(data.get("cid"))

    cart_item = get_object_or_404(CartItem, pk=cid)

    new_qty = cart_item.qty + qty
    if new_qty < 1:
        return JsonResponse({"status": "error", "message": "Quantity cannot be less than 1"})

    cart_item.qty = new_qty
    cart_item.save()

    return JsonResponse({"status": "success", "new_qty": cart_item.qty, "total": cart_item.sub_total()})


@login_required(login_url="login_user")
def checkout(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user)

    cart_items = CartItem.objects.filter(cart = cart)
    total = 0

    if not cart_items.exists():
        cart_items = []
        total = 0
    else:
        for items in cart_items:
            total += items.sub_total()

    context = {
        'cart_items' : cart_items,
        'total' : total,
        'is_empty' : not bool(cart_items),
    }

    return render(request, 'checkout.html', context)


def makePayment(request):
    amount_str = request.GET.get("amount")
    amount_float = float(amount_str)
    amount = int(amount_float)
    print(type(amount))

    client = razorpay.Client(auth=("rzp_test_wef6Tlaev3Pre9", "OeabKs2qmdPauM2RHWDQb9TG"))

    data = { "amount": amount*100 , "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) 

    return JsonResponse(payment)


@login_required(login_url="login_user")
def create_order(request):
    payment_id = request.GET.get('payment_id', 'N/A')

    # Fetch user's cart
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    
    # Create a new order
    order = Order.objects.create(
        user=request.user,
        total_price=cart.total_cart_price(),
        status='Completed',
        payment_id=payment_id,
        payment_type="Online"
    )
    
    # Add items to the order
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            # price=item.product.productPrice,
            qty=item.qty
        )

    # Optionally, clear the cart after order
    cart_items.delete()

    # **Redirect to order-success page with order ID**
    return JsonResponse({"status": "success", "redirect_url": f"/order-success/{order.id}/"})


@login_required(login_url="login_user")
def order_success(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)  # Fetch specific order

    context = {
        'ordered_items': order.order_items.all(),
        'payment_id': order.payment_id,
        'total_amount': order.total_price,
        'order_number': order.id,
    }
    return render(request, 'order-success.html', context)


@login_required(login_url="login_user")
def order_detail(request, order_id):
    order = Order.objects.filter(id=order_id, user=request.user).first()

    if not order:
        return render(
            request,
            'order_detail.html',
            {"order_not_found": True}
        )

    order.total_price = order.total_order_price()
    order.save()  

    order_items = order.order_items.all()

    return render(
        request,
        'order_detail.html',
        {
            'order': order,
            'ordered_items': order_items,
            'payment_id': order.payment_id,  
            'total_amount': order.total_price,
            "order_not_found": False
        }
    )






def whishlist(request):
    return render(request, "whishlist.html")

def features(request):
    return render(request, "features.html")

def blog(request):
    return render(request, "blog.html")

def blog_detail(request):
    return render(request, "blog-detail.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        data = request.POST
        username = data.get('loginusername')
        password = data.get('loginpassword')

        if not username or not password:
            messages.error(request, "Enter All Details !!!")
        else:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login Successfull !!!")
                return redirect("index")
            else:
                messages.error(request, "Enter Correct Details !!!")
                return render(request, "login.html")
    return render(request, "login.html")

def signup_user(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    pattern = "^[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]{2,4}$"
    
    if request.method == "POST":
        data = request.POST
        username = data.get('signupusername')
        email = data.get('signupemail')
        password = data.get('signuppassword')
        cpassword = data.get('confirmpassword')

        if not username or not email or not password or not cpassword:
            messages.error(request, "Enter All Details !!!")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User Already exist !!!")
            else:
                if password == cpassword:
                    user = User(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    messages.success(request, "Registration Successfull !!!")
                    return redirect("login_user")
                else:
                    messages.error(request, "Passwords do not match. Please ensure that both passwords are same.")
    return render(request, "login.html")

def logout_user(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logout Successfull !!!")
    return render(request, "login.html")

def help(request):
    return render(request, "help.html")


@login_required
def profile(request):
    # Get user address and wishlist
    addresses = Address.objects.filter(user=request.user)
    wishlist_items = Wishlist.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)  # Assuming you already have an Order model

    context = {
        'addresses': addresses,
        'wishlist_items': wishlist_items,
        'orders': orders,
    }
    return render(request, 'profile.html', context)

@login_required
def add_address(request):
    if request.method == "POST":
        house_no = request.POST['house_no']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        
        Address.objects.create(
            user=request.user,
            house_no=house_no,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code
        )
        return redirect('profile')

@login_required
def add_to_wishlist(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_url = request.POST['product_url']
        
        Wishlist.objects.create(
            user=request.user,
            product_name=product_name,
            product_url=product_url
        )
        return redirect('profile')




def my_orders(request):
    context = {
        # orders = Order.objects.filter(user=request.user).order_by('-created_at')
    }
    return render(request, 'my_orders.html', context)

def address_book(request):
    context = {
        # addresses = Address.objects.filter(user=request.user)
    }
    return render(request, 'address_book.html', context)

def acc_setting(request):
    return render(request, "acc_setting.html")

def my_wishlist(request):
    context = {
        # wishlist_items = Wishlist.objects.filter(user=request.user)
    } 
    return render(request, 'my_wishlist.html', context)




# extra:
def home2(request):
    return render(request, "home-02.html")

def home3(request):
    return render(request, "home-03.html")