
from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader.fields import RichTextUploadingField
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.shop.urls", namespace="shop")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


