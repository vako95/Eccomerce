from django.db import models
from django.urls import reverse

class SocialNetwork(models.Model):
    social = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="Social",
        help_text="The name of the social network",
    )
    url = models.URLField(
        blank=False,
        null=False,
        verbose_name="Social Network URL",
        help_text="The URL to the social network profile or page",
    )
    slug = models.SlugField(
        max_length=150,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug",
        help_text="A slug for the social network",
    )
    logo = models.ImageField(
        upload_to="social/%Y/%m/%d/",
        null=True,
        blank=True,
        verbose_name="Logo",
        help_text="Social Logo",
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Status",
        help_text="Check this box if the item is active. Uncheck to disable.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Date and time when the item was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Updated",
        help_text="Date and time of the last update.",
    )

    def __str__(self):
        return self.social

    def get_absolute_url(self):
        return reverse("shop:social_network_detail", kwargs={"social_network_slug":self.slug})
    
    class Meta:
        verbose_name = "Social Network"
        verbose_name_plural = "Social Networks"
        ordering = ("-created_at",)
