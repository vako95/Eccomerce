from django.contrib import admin
from django.utils.html import mark_safe, format_html
from django.templatetags.static import static
from ..models import Product


    


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title_tag","slug_with_link","poster_tag", "price_tag", "discount_tag", "tax_tag","final_price_tag","created_tag", "updated_tag","status")
    list_display_links = ("title_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("price","created_at","updated_at","status",)
    search_fields = ("title","slug")
    readonly_fields = ("poster_tag", "created_at","updated_at")
    exclude = ("slug",)
    

    @admin.display(description="Title")
    def title_tag(self,obj):
       title_display  = obj.title if len(obj.title) <= 12 else obj.title + "..."
       return mark_safe(f'{title_display}')
    
    class Media:
        css = {
            'all': static('shop/assets/admin/admin.css',)  
        }
    
    @admin.display(description="Content")
    def content_tag(self,obj):
        content_display = obj.content if len(obj.content) <= 12 else obj.content + "..."
        return mark_safe(f"{content_display}")
    
    @admin.display(description="Slug")
    def slug_with_link(self,obj):
        slug_link = obj.slug if len(obj.slug) <=12 else obj.slug + "..."
        slug_url = obj.get_absolute_url()
        return format_html(
            '<a href={} target="__blank">{} 🔗..</a>',
            slug_url,
            slug_link
        )
    


    @admin.display(description="Poster")
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
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(status=True)



    
    
    

    

