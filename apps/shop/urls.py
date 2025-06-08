from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index, name="home"),
    path("all_product/", views.all_product, name="all_product"),
    path("author_detail/<slug:author_slug>/", views.author_detail, name="author_detail"),
    path("trending_detail/<slug:product_slug>/", views.trending_detail, name="product_detail"),
    path("brand_detail/<slug:brand_slug>/", views.author_detail, name="brand_detail"),

]
