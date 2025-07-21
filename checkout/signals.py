"""
signals.py

In order to call the update_total method,
I have to use the django built in signals.

This file handles automatic operations triggered by model events,
such as updating the order total when a line item is saved or deleted.
TO let
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def handle_lineitem_save(sender, instance, created, **kwargs):
    """
    Signal handler that updates the related order's totals whenever
    an OrderLineItem is created or updated.

    Args:
        sender (Model): The model class sending the signal (OrderLineItem).
        instance (OrderLineItem): The actual instance being saved.
        created (bool): True if a new instance was created.
        **kwargs: Additional keyword arguments.
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def handle_lineitem_save(sender, instance, **kwargs):
    """
    Signal handler that updates the related order's totals
    when an OrderLineItem is deleted.
    """
    instance.order.update_total()
