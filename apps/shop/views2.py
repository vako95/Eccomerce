from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import *
from django.core.cache import cache

# def index(request):
#     trending_products = Product.objects.filter(status=True)
#     print(trending_products)
#     all_categories = cache.get("categories")
#     if not all_categories:
#         all_categories = (
#             Category.objects
#             .annotate(product_count=Count("products"))
#             .filter(status=True,products__gt=0)
#         )
#         cache.set("categories", all_categories)
#     context = {
#         "all_categories": all_categories,
#         "trending_products":trending_products
#     }
#     return render(request, "shop/index.html", context)


def index(request):
    categories = cache.get("categories")
    if not categories:
        categories = Category.objects.annotate(product_count=Count('products'))
        cache.set("categories", categories)
    context = {"all_categories": categories}
    return render(request, "shop/index.html", context)

def about(request):
    return render(request, "shop/about.html")

def product_detail(request, product_slug):
    context = {
        "product_detail": Product.objects.filter(slug=product_slug),
    }
    return render(request, "shop/product_detail.html", context)

def category_detail(request, category_slug):
    category_detail =Category.objects.prefetch_related("products").annotate(product_count=Count('products')).get(slug=category_slug)
    context = {
    "category_detail":category_detail
    }
    return render(request, "shop/shop-grid.html", context)

def author_detail(request):
    pass

def tag_detail(request):
    pass


def brand_detail(request):
    pass

def social_network(request):
    pass
