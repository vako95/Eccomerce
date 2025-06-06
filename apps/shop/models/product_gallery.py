from django.db import models
from ..models import Product 
from django.core.validators import FileExtensionValidator

class ProductGallery(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="gallery",
        on_delete=models.CASCADE,
        verbose_name="Product Gallery",
    )
    image = models.ImageField(
        upload_to="products/gallery/%Y/%d/%m/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["svg", "png", "jpg", "jpeg"]
            ),
        ],
        blank=True,
        null=True,
        verbose_name="Gallery",
        help_text="Upload an image"
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Alt Text",
        help_text="Text for SEO and accessibility (alt attribute)",
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name="Main Image",
        help_text="Check if this is the primary image for the product",
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Display Order",
        help_text="Controls the display order of the images",
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    uploaded_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Uploaded At",
    )

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        ordering = ("order",) 

    def __str__(self):
        return f"{self.product.title} - Image {self.id}"