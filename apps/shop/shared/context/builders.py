from ...models import *
from django.db.models import Count



def common_context():

    return {
        "all_products":Product.objects.all(),
        "all_categories":Category.objects.filter(status=True).annotate(product_count=Count('products')).filter(product_count__gt=0)
    }

def category_detail_context(category_slug):
    return {
         "category_detail":Category.objects.prefetch_related("products").get(slug=category_slug)
    }

