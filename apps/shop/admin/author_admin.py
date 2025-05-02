from django.contrib import admin
from django.utils.html import mark_safe, format_html
from django.templatetags.static import static
from ..models import Author

@admin.register(Author)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name_tag","bio_tag","slug_with_link","created_tag", "updated_tag","status")
    list_display_links = ("name_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("created_at","updated_at","status",)
    search_fields = ("name","slug")
    readonly_fields = ("poster_tag", "created_at","updated_at")
    exclude = ("slug",)
    

    @admin.display(description="name")
    def name_tag(self,obj):
       name_display  = obj.name if len(obj.name) <= 12 else obj.name + "..."
       return mark_safe(f'{name_display}')
    
    class Media:
        css = {
            'all': static('shop/assets/admin/admin.css',)  # Замените путь на актуальный путь к вашему файлу
        }
    
    @admin.display(description="Biography")
    def bio_tag(self,obj):
        bio_tag_display = obj.bio if len(obj.bio) <= 12 else obj.bio_tag + "..."
        return mark_safe(f"{bio_tag_display}")
    
    @admin.display(description="Slug")
    def slug_with_link(self,obj):
        slug_link = obj.slug if len(obj.slug) <=12 else obj.slug + "..."
        slug_url = obj.get_absolute_url()
        return format_html(
            '<a href={} target="__blank">{} 🔗..</a>',
            slug_url,
            slug_link
        )
    


    @admin.display(description="Image")
    def poster_tag(self, obj):
        if obj.poster:
            return mark_safe(
                f"<a href='{obj.poster.url}' data-lity><img class='preview__image' src='{obj.poster.url}' alt='Preview'></a>"
            )
        else:
            return mark_safe(
                f"<a href='{static("shop/assets/admin/img/no_image.jpg")}' data-lity><img class='preview__image' src='{static("shop/assets/admin/img/no_image.jpg")}' alt='Preview'></a>" 
            )
    

    class Media:
        css = {
        'all': (
            'shop/assets/lity/dist/lity.min.css',
            'shop/assets/admin/css/admin.css'
            )
        }
        js = (
        'shop/assets/lity/dist/lity.min.js',
        'shop/assets/lity/dist/lity.jquery.js',
        'shop/assets/lity/dist/lity.zepto.js',
        )

    @admin.display(description="Price")
    def price_tag(self,obj):
        return mark_safe(f'<span class="price">{obj.price}<span/>')

    @admin.display(description="Final Price")
    def final_price_tag(self, obj):
        return mark_safe(f'<span class="final_price">💰 {obj.get_final_price()}</span>')
    
    @admin.display(description=mark_safe("💸Discount"))
    def discount_tag(self, obj):
        return mark_safe(f'<span class="discount">{obj.discount}</span>')
    
    @admin.display(description=mark_safe("🧾Tax"))
    def tax_tag(self, obj):
        return mark_safe(f'<span class="tax">{obj.tax}</span>')
    
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
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(status=True)



    
    
    

    

