import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from ..models import Category

@receiver(pre_save, sender=Category)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)
