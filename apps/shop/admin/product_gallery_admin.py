from django.contrib import admin
from ..models import ProductGallery
from django.utils.html import format_html, mark_safe
from django.templatetags.static import static

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1 
    min_num = 0
    max_num = 5
    fields = ("image", "alt_text", "is_main", "order")
    readonly_fields = ("created_at","uploaded_at")
    
    

  