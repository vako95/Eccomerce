import math
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="Title",
        help_text="Enter the product name (max 255 characters).",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
        null=False,
        verbose_name="Slug",
        help_text= "Automatically generated based on the Title.",
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Content",
        help_text="Optional content or description.",
    )
    poster = models.FileField(
        upload_to="products/posters/%Y/%d/%m/",
        validators=[FileExtensionValidator(
            allowed_extensions=["jpg","jpeg","webp","png"]
        )],
        blank=True,
        null=True,
        verbose_name="Poster",
        help_text="Upload an image",
    )
    price = models.FloatField(
        blank=False,
        null=False,
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(10000000)],
        verbose_name="Price",
        help_text="Enter a value between 0 and 10,000,000."
    )
    discount = models.IntegerField(
        blank=True,
        null=False,
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    tax = models.FloatField(
        blank=True,
        null=False,
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(10000000)],
        verbose_name="Tax",
        help_text="Enter tax amount (0–10,000,000)."
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
        return self.title

    def get_final_price(self) -> int | float:
        price = float(("{:2g}").format(self.price - (self.price * (self.discount /100 )) + self.tax))
        return int(price) if price.is_integer() else price

    def get_tax(self) -> int | float:
        self.get_final_price() - self.tax
           
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)


class ProductByPrice(Product):
    class Meta:
        proxy = True
        ordering = ['-price'] 


    def is_expensive(self):
        return self.price > 1000
    
class SalesProduct(Product):  # Наследуемся от Product
    class Meta:
        verbose_name = "Endirimli Mehsullar"        # Название в админке (единственное число)
        verbose_name_plural = "Endirimli Mehsullar" # Название во множественном числе
        proxy = True 