from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="Name",
        help_text="Enter the name of the product."
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
        help_text= "Automatically generated based on the Name.",    
    )
    image = models.FileField(
        upload_to="category/%Y/%d/%m/",
        validators=[FileExtensionValidator(
            allowed_extensions=["jpg","jpeg","webp","png"]
        ),],
        blank=True,
        null=True,
        verbose_name="Image",
        help_text="Upload a category image"

    )
    status = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Indicates whether the item is active."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Date and time when the item was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated",
        help_text="Date and time of the last update."
    )

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self) -> str:
        return reverse("shop:category_detail", kwargs={"category_slug":self.slug})
    
    class Meta :
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("created_at",)
    