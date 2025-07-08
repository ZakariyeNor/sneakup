from django import template

register = template.Library()

# Template filter for calculating the subtotal
# of a product by multiplying its price and quantity
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a product.

    Multiplies the product price by the quantity ordered.

    Args:
        price (int | float | Decimal): The price of a single product unit.
        quantity (int): The number of units ordered.

    Returns:
        Numeric value representing the subtotal.
    """
    return price * quantity


# Template filter for multiplying a value
# with a rate, used for VAT calculation
@register.filter(name='multiply_vat')
def multiply_vat(value, arg):
    """
    Multiply two numeric values, typically used for calculating VAT.

    Args:
        value (int | float | Decimal): The base number (e.g., subtotal).
        arg (int | float | Decimal): The multiplier (e.g., VAT rate like 0.06).

    Returns:
        Result of the multiplication, or an empty string if invalid input is encountered.
    """
    try:
        return value * arg
    except (TypeError, ValueError):
        return ''
