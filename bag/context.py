from django.shortcuts import get_object_or_404
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP
from products.models import Product



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
    total_items = 0
    total_price = 0

    # Retrieve shopping bag info from the session.
    bag = request.session.get('bag', {})


    # Add its current contents to the context
    # to show the total cost on all pages.
    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        # Chech if the product has size with quantity
        if isinstance(item_data, int):
            # If the quantity is only integer
            # Then quantity is equal to item_data
            quantity = item_data
            # Then add dictionary to the list of bag items
            selected_size = None
            print(f"Item: {product.name}, Size: {selected_size}, Quantity: {quantity}")
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'selected_size': None,
            })

            # Calculate the total price
            total_price += product.price * quantity
            # Increment total items in the bag by quantity
            total_items += quantity

        else:
            if isinstance(item_data, dict):
                for size, quantity in item_data.items():
                    selected_size = size
                    print(f"Item: {product.name}, Size: {selected_size}, Quantity: {quantity}")
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'selected_size': size,

                    })

                    # Calculate the total price
                    total_price += product.price * quantity
                    # Increment total items in the bag by quantity
                    total_items += quantity


    if total_price < settings.FREE_DELIVERY:
        delivery_cost = total_items * (Decimal(str(settings.DELIVERY_PERCENTAGE)) / Decimal('100'))
        free_delivery = settings.FREE_DELIVERY - total_price
        
    else:
        delivery_cost = Decimal('0.00')
        free_delivery = Decimal('0.00')
    
    vat_rate = Decimal(str(settings.EASTIMATED_VAT)) / Decimal('100')
    subtotal = total_price
    # Calculate the total products price plus VAT and round up
    est_vat = (subtotal * vat_rate).quantize(Decimal('0.01'), ROUND_HALF_UP)

    # Calculate the grand total and round up
    grand_total = (subtotal + delivery_cost + est_vat).quantize(Decimal('0.01'), ROUND_HALF_UP)
    
    context = {
        'bag_items': bag_items,
        'total_items': total_items,
        'total_price': total_price,
        'delivery_cost': delivery_cost,
        'free_delivery': free_delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY,
        'grand_total': grand_total,
        'subtotal': subtotal,
        'est_vat': est_vat,
        'vat_rate': vat_rate,
    }

    return context

