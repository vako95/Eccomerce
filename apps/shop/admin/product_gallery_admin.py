from django.contrib import admin
from ..models import ProductGallery
from django.utils.html import format_html, mark_safe
from django.templatetags.static import static

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1 
    min_num = 0
    max_num = 5
    fields = ("image_tag", "alt_text", "is_main", "order")
    readonly_fields = ("image_tag","created_at","uploaded_at")
    
    @admin.display(description="Gallery")
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
            f'<div class="preview__link">'
            f'<a href="{obj.image.url}" data-lity>'
            f'<img class="preview__image" src="{obj.image.url}" alt="Preview">'
            f'</a></div>'
        )
        else:
         no_image_url = static("shop/admin/assets/image/no_image.png")
        return mark_safe(
            f'<div class="preview__link">'
            f'<a href="{no_image_url}" data-lity>'
            f'<img class="preview__image" src="{no_image_url}" alt="No image">'
            f'</a></div>'
        )

  