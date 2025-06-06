from django.contrib import admin
from ..models import Product
from .product_gallery_admin import ProductGalleryInline
from django.utils.html import mark_safe,format_html
from django.templatetags.static import static

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGalleryInline]
    list_display = (
        "title_tag",
        "slug_with_link",
        "poster_tag",
        "price_tag",
        "discount_tag",
        "tax_tag",
        "final_price_tag",
        "created_tag",
        "updated_tag",
        "status",
        )
    list_display_links = ("title_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("price","created_at","updated_at","status",)
    search_fields = ("title","slug")
    readonly_fields = ("poster_tag", "created_at","updated_at")
    exclude = ("slug",)

    @admin.display(description="Title")
    def title_tag(self,obj):
        title_display = obj.title if len(obj.title) <= 12 else obj.title + "..."
        return mark_safe(f"{title_display}")
    
    class Media:
        css = {
            "all":("shop/admin/assets/css/style.css",)
        }
    
    @admin.display(description="Slug")
    def slug_with_link(self,obj):
        slug_display = obj.slug if len(obj.slug) <= 12 else obj.slug + "🔗.."
        return mark_safe(f'<a>{slug_display}</a>') 

    @admin.display(description="Poster")
    def poster_tag(self,obj):
        if obj.poster :
            return mark_safe(
                f'<div class="preview__link"><a href="{obj.poster.url}" data-lity>' 
                f'<img class="preview__image" src="{obj.poster.url}" alt="Preview">'
                f'</a> </div>')
        else:
            no_image_url = static("shop/admin/assets/image/no_image.png")
        return mark_safe(
            f'<div class="preview__link">'
            f'<a href="{no_image_url}" data-lity>'
            f'<img class="preview__image" src="{no_image_url}" alt="No image">'
            f'</a></div>'
        )
        
    class Media:
        css = {
            "all": (
                "shop/lity/dist/lity.min.css",
                "shop/admin/assets/css/style.css"
            )
        }
        js = {
        'shop/lity/vendor/jquery.js',
        'shop/lity/vendor/zepto.js',
        'shop/lity/vendor/lity.min.js',
        }

    @admin.display(description="Price")
    def price_tag(self,obj):
           return mark_safe(f'<span class="price">{obj.price}<span/>')
    
    @admin.display(description="💸Discount")
    def discount_tag(self,obj):
           return mark_safe(f'<span class="discount">{obj.discount}<span/>')
    
    @admin.display(description=mark_safe("🧾Tax"))
    def tax_tag(self, obj):
        return mark_safe(f'<span class="tax">{obj.tax}</span>')
    
    @admin.display(description="Final Price")
    def final_price_tag(self, obj):
        return mark_safe(f'<span class="final_price">💰 {obj.get_final_price()}</span>')
    
    @admin.display(description="Created")
    def created_tag(self, obj):
        return format_html(
            '<span style="color: green;">{}</span>',
            obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
        )

    @admin.display(description="Updated")
    def updated_tag(self, obj):
        return format_html(
            '<span style="color: orange;">{}</span>',
            obj.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        )


