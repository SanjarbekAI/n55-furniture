from django.db.models.signals import pre_save
from django.dispatch import receiver

from app_products.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def update_product_price(sender, instance, **kwargs):
    if instance.discount:
        instance.discount_price = instance.price - (instance.price * instance.discount / 100)
    else:
        instance.discount_price = instance.price
