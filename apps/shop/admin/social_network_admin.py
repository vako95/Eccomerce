from django.contrib import admin
from ..models import SocialNetwork
from django.utils.html import mark_safe, format_html
from django.templatetags.static import static


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        "social_tag",
        "slug_with_link",
        "logo_tag",
        "created_tag",
        "updated_tag",
        "status",
        )
    list_display_links = ("social_tag",)
    list_filter = ("updated_at", "created_at","status")
    list_editable = ("status",)
    search_fields = ("social",)
    readonly_fields = ("logo_tag","created_at","updated_at")
    list_per_page = 10
    exclude = ("slug",)

    @admin.display(description="Social")
    def social_tag(self,obj):
        display_social = obj.social if len(obj.social) <= 12 else obj.social + "..."
        return mark_safe(f"{display_social}")
    
    css = {
        "shop/admin/assets/css/style.css"
    }
    
    @admin.display(description="Slug")
    def slug_with_link(self,obj):
        slug_display = obj.slug if len(obj.slug) <= 12 else obj.slug + "🔗.."
        return mark_safe(f'<a>{slug_display}</a>') 

    @admin.display(description="Created")
    def created_tag(self, obj):
        return format_html(
            '<span class="time_create">{}</span>',
            obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
        )
    
    class Media:
        css = {
        "shop/admin/assets/css/style.css"
        }

    @admin.display(description="Updated")
    def updated_tag(self, obj):
        return format_html(
            '<span class="time_update">{}</span>',
            obj.created_at.strftime("%Y-%m-%d %H:%M:%S")
        )
    
    class Media:
        css = {
        "shop/admin/assets/css/style.css"
        }    

    @admin.display(description="Poster")
    def logo_tag(self,obj):
        if obj.logo :
            return mark_safe(
                f'<div class="preview__link_social"><a href="{obj.logo.url}" data-lity>' 
                f'<img class="preview__image_social" src="{obj.logo.url}" alt="Preview">'
                f'</a> </div>')
        else:
            no_logo_url = static("shop/admin/assets/image/no_image.png")
        return mark_safe(
            f'<div class="preview__link_social">'
            f'<a href="{no_logo_url}" data-lity>'
            f'<img class="preview__image_social" src="{no_logo_url}" alt="No image">'
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


    