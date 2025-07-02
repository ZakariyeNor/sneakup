from django.conf import settings
from decimal import Decimal



def bag_contents(request):
    """
    Render the shopping bag page with current bag contents and totals.

    Retrieves the user's current shopping bag from the session,
    calculates the total price(delivery cost and product cost), quantity and selected product sizes.

    Context variables include:
      - List of items currently in the bag
      - Total number of items
      - Total cost of all items in the bag
      - Calculated delivery fee
      - Check if user qualifies for free delivery
      - Total including delivery

    """

    bag_items = []
    product_count = 0
    total_price = 0
    
    if total_price < settings.FREE_DELIVERY:
        delivery_fee = total_price * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery = total_price - settings.FREE_DELIVERY
    else:
        delivery_fee = 0
        free_delivery = 0
    
    grand_total = delivery_fee + total_price
