"""
URL configuration for django_ecommerce_theme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('address/', views.address, name='address'),
    path('alerts/', views.alerts, name='alerts'),
    path('blog-full-width/', views.blog_full_width, name='blog-full-width'),
    path('buttons/', views.buttons, name='buttons'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('empty-cart/', views.empty_cart, name='empty-cart'),
    path('faq/', views.faq, name='faq'),
    path('forget-password/', views.forget_password, name='forget-password'),
    path('order/', views.order, name='order'),
    path('pricing/', views.pricing, name='pricing'),
    path('product-single/', views.product_single, name='product-single'),
    path('profile-details/', views.profile_details, name='profile-details'),
    path('purchase-confirmation/', views.purchase_confirmation, name='purchase-confirmation'),
    path('shop/', views.shop, name='shop'),
    path('shop-sidebar/', views.shop_sidebar, name='shop-sidebar'),
    path('signin/', views.signin, name='signin'),
    path('typography/', views.typography, name='typography'),

    path('orders', views.orders, name='orders'),
    path('blog-grid/', views.blog_grid, name='blog-grid'),
    path('blog-left-sidebar/', views.blog_left_sidebar, name='blog-left-sidebar'),
    path('blog-right-sidebar/', views.blog_right_sidebar, name='blog-right-sidebar'),
    path('blog-single/', views.blog_single, name='blog-single'),
    path('not-found/', views.not_found, name='not-found')

]
