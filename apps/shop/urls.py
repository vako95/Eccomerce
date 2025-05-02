from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("product/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("category_detail/<slug:category_slug>/", views.category_detail, name="category_detail"),
    path("author_detail/<slug:author_slug>/", views.author_detail, name="author_detail"),
    path("tag_detail/<slug:tag_slug>/", views.tag_detail, name="tag_detail"),
    path("brand_detail/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
    path("social_network_detail/<slug:social_network_slug>/", views.social_network, name="social_network_detail"),
]