"""
URL configuration for eZcart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('home2', views.home2, name="home2"),
    path('home3', views.home3, name="home3"),
    path('shop', views.shop, name="shop"),
    path('shoping-cart', views.shoping_cart, name="shoping-cart"),
    path('whishlist', views.whishlist, name="whishlist"),
    path('product-detail', views.product_detail, name="product-detail"),
    path('features', views.features, name="features"),
    path('blog', views.blog, name="blog"),
    path('blog-detail', views.blog_detail, name="blog-detail"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('checkout', views.checkout, name="checkout"),
    path('login_user', views.login_user, name="login_user"),
    path('signup_user', views.signup_user, name="signup_user"),
    path('logout', views.logout_user, name="logout"),
    path('help', views.help, name="help"),
    path('get_products_by_category', views.get_products_by_category, name="get_products_by_category"),
    path('searchProduct', views.searchProduct, name="searchProduct"),

    path('profile', views.profile, name="profile"),
    path('profile/', include([
        path('my_orders', views.my_orders, name="my_orders"),
        path('my_wishlist', views.my_wishlist, name="my_wishlist"),
        path('address_book', views.address_book, name="address_book"),
        path('acc_setting', views.acc_setting, name="acc_setting"),
    ])),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)