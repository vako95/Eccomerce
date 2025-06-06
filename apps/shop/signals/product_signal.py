import uuid
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import Product

@receiver(pre_save,sender=Product)
def generate_product_slug(sender, instance, **kwargs):
    if not instance.slug:
        unique_suffix = str(uuid.uuid4())[:8]
        instance.slug = f"{slugify(instance.title)}-{unique_suffix}"

