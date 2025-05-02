from django.contrib import admin
from django.utils.html import format_html, mark_safe
from django.templatetags.static import static

from ..models import SocialNetwork


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = (
        "social_tag",
        "slug",
        "logo_tag",
        "status",
        "created_tag", 
        "updated_tag",
    )
    list_display_links = ("social_tag",)
    list_editable = ("status",)
    list_per_page = 10
    list_filter = ("created_at","updated_at","status",)
    search_fields = ("social","slug")
    readonly_fields = ("logo_tag", "created_at","updated_at")
    exclude = ("slug",)

    @admin.display(description="social")
    def social_tag(self,obj):
       social_display  = obj.social if len(obj.social) <= 12 else obj.social + "..."
       return mark_safe(f'{social_display}')
    
    class Media:
        css = {
            'all': static('shop/assets/admin/admin.css',)  
        }


    # @admin.display(description="Slug")
    # def slug_with_link(self,obj):
    #     slug_link = obj.slug if len(obj.slug) <= 12 else obj.slug[:12] + "..."
    #     slug_url = obj.get_absolute_url()
    #     return format_html(
    #         '<a href={} target="__blank">{} 🔗..</a>',
    #         slug_url,
    #         slug_link
    #     )

    @admin.display(description="Image")
    def logo_tag(self, obj):
        if obj.logo:
            return mark_safe(
                f"<a href='{obj.logo.url}' data-lity><img class='preview__image' src='{obj.logo.url}' alt='Preview'></a>"
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