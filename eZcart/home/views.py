from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def shop(request):
    return render(request, "shop.html")

def shoping_cart(request):
    return render(request, "shoping-cart.html")

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