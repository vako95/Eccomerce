from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.index),
    path("author_detail/<slug:author_slug>/", views.author_detail, name="author_detail"),
    path("brand_detail/<slug:brand_slug>/", views.author_detail, name="brand_detail"),

]
