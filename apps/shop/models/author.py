from django.db import models
from django.urls import reverse

class Author(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Username",
        help_text="Enter username"
    )
    password = models.CharField(
        max_length=128,
        verbose_name="Password",
        help_text="Enter your password"
    )
    email = models.EmailField(
        max_length=250,
        unique=True,
        verbose_name="Email",
        help_text="Enter your email"
    )
    name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text="Author’s name"
    )
    
    surname = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="Surname",
        help_text="Enter last name"
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
        help_text="Automatically generated based on the Name.",
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        verbose_name="Gender",
        help_text="Select gender"
    )
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Age",
        help_text="Enter age in years"
    )
    bio = models.TextField(
        blank=True,
        verbose_name="Biography",
        help_text="Enter a short biography of the author"
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

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def get_absolute_url(self):
       return reverse("shop:author_detail", kwargs={"author_slug":self.slug})
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ("-created_at",)