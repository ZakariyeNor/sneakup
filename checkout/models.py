from django.db import models
import uuid
from djang.conf import settings
from djang.db.models import sum
from products.models import Product

# Order Model
class Order(models.Model):
    """
    A model representing a customer's order, including personal details,
    shipping information, delivery costs, and order totals.
    """

    order_number = models.UUIDField(max_length=15, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(max_length=99, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    country = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    street_address_1 = models.CharField(max_length=255, blank=False, null=False)
    street_address_2 = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.CharField(max_length=20, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f"Order {self.order_number} - {self.first_name} {self.last_name}"


class OrderLineItem(models.Model):
    """
    A model representing a single line item within an order.

    Each line item links to a specific product, optionally includes a size, 
    and stores the quantity and total cost for that product.
    """

    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=False, null=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False, editable=False)

    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} on order {self.order.order_number}"