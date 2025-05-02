from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from django.utils import timezone
from .author import Author
from .category import Category
from .brand import Brand
from .tag import Tag
from PIL import Image  

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Title",
        help_text="Enter the product title (max 255 characters).",
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=True,
        unique=True,
        verbose_name="Slug",
        help_text="Automatically generated based on the Title.",
    )
    content = models.TextField(
        null=False,
        blank=True,
        verbose_name="Content",
        help_text="Content about product"
    )
    poster = models.FileField(
        upload_to="%Y/%m/%d/",
        validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),
        ],
        blank=True,
        null=True,
        verbose_name="Poster",
        help_text="Upload an image"
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
        verbose_name="Discount (%)",
        help_text="Enter a value from 0 to 100."
    )
    tax = models.FloatField(
        blank=True,
        null=False,
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(10000000)],
        verbose_name="Tax",
        help_text="Enter tax amount (0–10,000,000)."
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Author",       
        help_text="Select product author",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="products",
        verbose_name="Category",
        help_text="Select a Category for the product.",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Brand",
        help_text="Pick a brand (or skip)"
    ) 
    tag = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="products",
        verbose_name="Tag",
        help_text="Select a Tag for the product.",
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

    # def save(self):
    #     super().save()  

    #     img = Image.open(self.poster.path) 

    #     if img.height > 300 or img.width > 300:
    #         new_img = (300, 300)
    #         img.thumbnail(new_img)
    #         img.save(self.poster.path) 

    @property
    def is_new(self):
        return (timezone.now() - self.created_at).days <= 15
    
    @property
    def is_hot(self):
        return self.discount >= 20 
    

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"product_slug":self.slug})
    
    def get_final_price(self) -> int | float:
        price = float(("{:2g}").format(self.price - (self.price * (self.discount /100 )) + self.tax))
        return int(price) if price.is_integer() else price 
    
    def get_price_without_tax(self) -> int | float:
        return self.get_final_price() - self.tax

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("-created_at",)
    
    


    

