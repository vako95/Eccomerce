from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
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
        upload_to="%Y/%m/%d/",
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp','svg']),
        ],
        blank=True,
        null=True,
        verbose_name="Poster",
        help_text="Upload an image"
    )
    status = models.BooleanField(
        default=True, 
        verbose_name="Status",
        help_text="Check this box if the item is active. Uncheck to disable.",
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


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:category_detail", kwargs={"category_slug":self.slug})
    
    class Meta:
        verbose_name ="Category"
        verbose_name_plural = "Categories"
        ordering = ("created_at",)