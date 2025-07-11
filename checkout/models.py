from django.db import models
import uuid
from django.conf import settings
from django.db.models import Sum
from products.models import Product
from decimal import Decimal, ROUND_HALF_UP

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
    delivery = models.DecimalField(max_digits=20, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    vat = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    # Generate order number method
    def _generate_order_number(self):
        """
        Using UUID generate random and unique order number
        """
        return uuid.uuid4().hex.upper()
    
    def save(self, *args, **kwargs):
        """
        Override the default save method to set the
        order number if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
    
    def update_total(self):
        """
        Update the grand total when a line item is added.
        So add a new field to the query set and then get
        and set the order total to that using Sum function.
        """
        # Safely sum lineitem totals; fallback to 0 if there are no items
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        # Calculate the delivery cost and roud up
        if self.order_total < settings.FREE_DELIVERY:
            self.delivery = (self.order_total * settings.DELIVERY_PERCENTAGE / 100).quantize(Decimal('0.01'), ROUND_HALF_UP)
        else:
            self.delivery = 0

        # Calculate the vat rate and round up
        vat_rate = Decimal(str(settings.ESTIMATED_VAT)) / Decimal('100')
        self.vat = (self.order_total * vat_rate).quantize(Decimal('0.01'), ROUND_HALF_UP)

        # Calculte the grand total and round up
        self.grand_total = (self.order_total + self.delivery + self.vat).quantize(Decimal('0.01'), ROUND_HALF_UP)
        self.save()


    def __str__(self):
        """
        Return a concise string representation of the order with customer and date.
        """
        return f"Order #{self.order_number} - {self.first_name} {self.last_name} on {self.date.strftime('%Y-%m-%d %H:%M')}"

# Order line item model
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
        """
        Calculate and set the line item total based on the product price and quantity
        before saving the instance to the database.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Return a readable string representation of the order line item,
        to identify the specific order item clearly in logs and admin interfaces.
        """
        size_str = f"(Size {self.product_size})" if self.product_size else ""
        return f"Order Item: {self.quantity} × {self.product.name}{size_str} (SKU: {self.product.sku}) — Part of Order #{self.order.order_number}"

