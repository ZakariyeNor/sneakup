from django.shortcuts import render, redirect, reverse
from .models import Order
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings

# Checkout View
def checkout(request):

    # Get the bag
    bag = request.session.get('bag', {})
    # Check the bag
    if not bag:
        # If the bag is empty, redirect to shop page('products') with an error message
        messages.error(
            request,
            "There's nothing in your bag at the moment"
        )
        return redirect(reverse('products'))

    # Otherwise create the order form to display
    # the ordered products in the bag
    order_form = OrderForm()
    
    #  Define the template and context
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'client_secret': 'secret ert',
    }

    # Render the checkout page
    return render(request, template, context)