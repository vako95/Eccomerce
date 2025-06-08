from django.shortcuts import render, get_object_or_404
from .models import Author, Product

def index(request):
    trending_products = Product.objects.filter(status=True)
    
    context = {
        "products":trending_products
    }
    return render(request, "public/index.html",context)

def all_product(request):
    all_products = Product.objects.filter(status=True)
    context = {
        "all_products":all_products
    }
    return render(request, "shop/all_product.html", context)

def trending_detail(request,product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {
      "product":product
    }
    return render(request, "shop/product_detail.html", context)

def author_detail(request):
    pass
