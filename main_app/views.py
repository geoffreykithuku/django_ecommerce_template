from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def address(request):
    return render(request, 'address.html')


def alerts(request):
    return render(request, 'alerts.html')


def blog_full_width(request):
    return render(request, 'blog-full-width.html')


def buttons(request):
    return render(request, 'buttons.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def coming_soon(request):
    return render(request, 'coming-soon.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def empty_cart(request):
    return render(request, 'empty-cart.html')


def faq(request):
    return render(request, 'faq.html')


def forget_password(request):
    return render(request, 'forget-password.html')


def order(request):
    return render(request, 'order.html')


def pricing(request):
    return render(request, 'pricing.html')


def product_single(request):
    return render(request, 'product-single.html')


def profile_details(request):
    return render(request, 'profile-details.html')


def purchase_confirmation(request):
    return render(request, 'purchase-confirmation.html')


def shop(request):
    return render(request, 'shop.html')


def shop_sidebar(request):
    return render(request, 'shop-sidebar.html')


def signin(request):
    return render(request, 'signin.html')


def typography(request):
    return render(request, 'typography.html')


def not_found(request):
    return render(request, '404.html')


def orders(request):
    return render(request, 'orders.html')


def blog_grid(request):
    return render(request, 'blog-grid.html')


def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')


def blog_right_sidebar(request):
    return render(request, 'blog-right-sidebar.html')


def blog_single(request):
    return render(request, 'blog-single.html')


