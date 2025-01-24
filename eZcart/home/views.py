from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'is_index': True,  # Flag for index page
    }
    return render(request, "index.html", context)

def shop(request):
    return render(request, "shop.html")

def shoping_cart(request):
    return render(request, "shoping-cart.html")

def whishlist(request):
    return render(request, "whishlist.html")

def product_detail(request):
    return render(request, "product-detail.html")

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

def checkout(request):
    return render(request, "checkout.html")

def login_user(request):
    return render(request, "login.html")

def help(request):
    return render(request, "help.html")






# extra:
def home2(request):
    return render(request, "home-02.html")

def home3(request):
    return render(request, "home-03.html")