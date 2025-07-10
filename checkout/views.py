from django.shortcuts import render, redirect, reverse
from .models import Order
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings

# Get bag contents from the context file in bag app
from bag.context import bag_contents

# Import stripe
import stripe


# Checkout View
def checkout(request):
    # Get stripe public key
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # Get stripe secret key
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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
    
    # Get the grand total from the current bag 
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    # Then convert grand total from euros to cents,
    stripe_total = round(total * 100)

    # Set the secret key on the stripe
    stripe.api_key = stripe_secret_key

    # Then create payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    # Make sure the api key is profided
    if not stripe_public_key:
        messages.warning(
            request, 'Stripe public key is missing.'
        )

    # The order form
    order_form = OrderForm()
    
    #  Define the template and context
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    # Render the checkout page
    return render(request, template, context)