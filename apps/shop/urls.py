from django.urls import path
from . import views
app_name = "shop"

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("product/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("category_all/", views.category_all, name="category_all"),
    path("category_detail/<slug:category_slug>/", views.category_detail, name="category_detail"),
    path("all_product/", views.all_product, name="all_product"),
    path("product_detail/<slug:product_slug>/", views.product_detail, name="product_detail"),
    path("create_product/", views.create_product  ,name="create_product"),
    path("author_detail/<slug:author_slug>/", views.author_detail, name="author_detail"),
    path("tag_detail/<slug:tag_slug>/", views.tag_detail, name="tag_detail"),
    path("brand_detail/<slug:brand_slug>/", views.brand_detail, name="brand_detail"),
    path("social_network_detail/<slug:social_network_slug>/", views.social_network, name="social_network_detail"),


    path("login/", views.login_view, name ="login"),
    path("logout/", views.logout_view, name ="logout"),
    path("register/", views.register_view, name="register_view")
]