from django.contrib import admin
from ..models import Author
from django.utils.html import mark_safe, format_html
from django.templatetags.static import static

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name_tag",
        "surname_tag",
        "slug_with_link",
        "photo_tag",
        "bio_tag",
        "created_tag",
        "updated_tag",
    )
    list_display_links = ("name_tag", "surname_tag")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "slug", "surname")
    readonly_fields = ("photo_tag", "created_at", "updated_at")
    exclude = ("slug",)

    @admin.display(description="Name")
    def name_tag(self, obj):
        return obj.name if len(obj.name) <= 12 else obj.name[:12] + "..."

    @admin.display(description="Surname")
    def surname_tag(self, obj):
        return obj.surname if len(obj.surname) <= 12 else obj.surname[:12] + "..."

    @admin.display(description="Biography")
    def bio_tag(self, obj):
        return obj.bio if len(obj.bio) <= 12 else obj.bio[:12] + "..."

    @admin.display(description="Slug")
    def slug_with_link(self, obj):
        slug_link = obj.slug if len(obj.slug) <= 12 else obj.slug[:12] + "..."
        slug_url = obj.get_absolute_url()
        return format_html(
        '<a href="{}" target="_blank">{} 🔗</a>',
        slug_url,
        slug_link
    )

    


    @admin.display(description="Poster")
    def photo_tag(self,obj):
        if obj.photo :
            return mark_safe(
                f'<div class="preview__link"><a href="{obj.photo.url}" data-lity>' 
                f'<img class="preview__image" src="{obj.photo.url}" alt="Preview">'
                f'</a> </div>')
        else:
            no_photo_url = static("shop/admin/assets/image/no_image.png")
        return mark_safe(
            f'<div class="preview__link">'
            f'<a href="{no_photo_url}" data-lity>'
            f'<img class="preview__image" src="{no_photo_url}" alt="No image">'
            f'</a></div>'
        )
        
    class Media:
            css = {
            "all": (
                "shop/lity/dist/lity.min.css",
                "shop/admin/assets/css/style.css"
                )}
            js = {
                'shop/lity/vendor/jquery.js',
                'shop/lity/vendor/zepto.js',
                'shop/lity/vendor/lity.min.js',
                }

    @admin.display(description="Created")
    def created_tag(self, obj):
        return format_html('<span style="color: green;">{}</span>', obj.created_at.strftime("%Y-%m-%d %H:%M:%S"))

    @admin.display(description="Updated")
    def updated_tag(self, obj):
        return format_html('<span style="color: orange;">{}</span>', obj.updated_at.strftime("%Y-%m-%d %H:%M:%S"))

    def get_queryset(self, request):
        return super().get_queryset(request).filter(status=True)

    class Media:
        css = {
            "all": [
                static("shop/assets/lity/dist/lity.min.css"),
                static("shop/assets/admin/css/admin.css"),
                static("shop/admin/assets/css/style.css"),
            ]
        }
        js = (
            "shop/assets/lity/dist/lity.min.js",
            "shop/assets/lity/dist/lity.jquery.js",
            "shop/assets/lity/dist/lity.zepto.js",
        )

    
    
    

    

         