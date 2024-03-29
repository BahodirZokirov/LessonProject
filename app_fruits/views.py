from django.shortcuts import render
from .models import Products


def home_page(request):
    if 'search' in request.GET:
        products = Products.objects.filter(product_description__icontains=request.GET['search'])
    else:
        products = Products.objects.all()
    context = {
        "products": products
    }
    return render(request, 'index.html', context)


def shop_page(request):
    return render(request, 'shop.html')


def shop_detail_page(request):

    return render(request, 'shop-detail.html')


def cart_page(request):
    return render(request, 'cart.html')


def chackout_page(request):
    return render(request, 'chackout.html')


def testimonial_page(request):
    return render(request, 'testimonial.html')


def contact_page(request):
    return render(request, 'contact.html')


def not_found_page(request):
    return render(request, '404.html')


def search_function(request):
    if "search" in request.GET:
        products = Products.objects.filter(peoduct_description__icontains=request.GET['search'])
    else:
        products = Products.objects.all()
    context = {
        "product": products
    }
    return render(request, 'index.html', context)
