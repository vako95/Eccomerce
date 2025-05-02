import uuid
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from ..models import Brand


@receiver(pre_save, sender=Brand)
def generate_brand_slug(sender, instance, **kwargs):
    if not instance.slug:
        unique_suffix = str(uuid.uuid4())[:8]
        instance.slug = f"{slugify(instance.name)}-{unique_suffix}"
