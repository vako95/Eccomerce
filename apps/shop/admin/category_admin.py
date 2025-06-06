from django.contrib import admin
from django.templatetags.static import static
from django.utils.html import format_html, mark_safe
from ..models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name_tag",
        "slug_with_link",
        "image_tag",
        "status",
        "created_tag", 
        "updated_tag",
    )
    list_display_links = ("name_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("created_at","updated_at","status",)
    search_fields = ("name","slug")
    readonly_fields = ("image_tag", "created_at","updated_at")
    exclude = ("slug",)

    @admin.display(description="Name")
    def name_tag(self,obj):
       name_display  = obj.name if len(obj.name) <= 12 else obj.name + "..."
       return mark_safe(f'{name_display}')
    
    class Media:
        css = {
            'all': static('shop/assets/admin/admin.css',)  
        }


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
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f"<a href='{obj.image.url}' data-lity><img class='preview__image' src='{obj.image.url}' alt='Preview'></a>"
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