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
    path('addToCart', views.addToCart, name="addToCart"),
    path('remove_from_cart', views.remove_from_cart, name="remove_from_cart"),
    path('changeQty', views.changeQty, name="changeQty"),
    path('makePayment', views.makePayment, name="makePayment"),
    path('create-order/', views.create_order, name="create-order"),
    path('order-success/<int:order_id>/', views.order_success, name="order_success"),
    path('order-success/<int:order_id>/', views.order_success, name="order_success"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("remove-from-wishlist/", views.remove_from_wishlist, name="remove_from_wishlist"),
    path("toggle-wishlist", views.toggle_wishlist, name="toggle-wishlist"),
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
    path('get_products_by_category_on_index', views.get_products_by_category_on_index, name='get_products_by_category_on_index'),
    path('searchProduct', views.searchProduct, name="searchProduct"),

    path('profile', views.profile, name="profile"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),

    # path('profile/', include([
    #     path('my_orders', views.my_orders, name="my_orders"),
    #     path('my_wishlist', views.my_wishlist, name="my_wishlist"),
    #     path('address_book', views.address_book, name="address_book"),
    #     path('acc_setting', views.acc_setting, name="acc_setting"),
    # ])),
    
    path('home-02/', views.home2, name='home-2'),
    path('home-03/', views.home3, name='home-3'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)