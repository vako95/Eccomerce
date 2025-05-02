import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from ..models import Author

@receiver(pre_save, sender=Author)
def generate_authro_slug(sender, instance,**kwargs):
    if not instance.slug:
        unique_suffix = str(uuid.uuid4())[:8]
        instance.slug = f"{slugify(instance.name)}-{unique_suffix}"