from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        'is_index': True,  # Flag for index page
    }
    return render(request, "index.html", context)

def shop(request):
    return render(request, "shop.html")

@login_required(login_url="login_user")
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

def profile(request):
    if request.user.is_anonymous:
        return redirect("login_user")
    return render(request, "profile.html")

def help(request):
    return render(request, "help.html")






# extra:
def home2(request):
    return render(request, "home-02.html")

def home3(request):
    return render(request, "home-03.html")