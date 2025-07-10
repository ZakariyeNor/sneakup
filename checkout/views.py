from django.shortcuts import render, redirect, reverse
from .models import Order, OrderLineItem
from products.models import Product
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

    # Check the method and get the bag if it's post
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        # Get form data 
        form_data = {
            'first_name':     request.POST.get('first_name', '').strip(),
            'last_name':      request.POST.get('last_name', '').strip(),
            'email':          request.POST.get('email', '').strip(),
            'phone_number':   request.POST.get('phone_number', '').strip(),
            'street_address_1': request.POST.get('street_address_1', '').strip(),
            'street_address_2': request.POST.get('street_address_2', '').strip(),
            'city':           request.POST.get('city', '').strip(),
            'postcode':       request.POST.get('postcode', '').strip(),
            'county':         request.POST.get('county', '').strip(),
            'country':        request.POST.get('country', '').strip(),
        }
        # Bind the submitted form data to an
        # OrderForm instance for validation
        order = order_form = OrderForm(form_data)

        # Check if the form is valid and save if it's
        if order_form.is_valid():
            order_form.save()
            
            for item_id, item_data in bag.items():
                try:
                    # Retrieve the Product or return 404 if it doesn’t exist
                    product = get_object_or_404(Product, pk=item_id)

                    # FREE‑SIZE PRODUCTS: item_data is an integer quantity
                    if isinstance(item_data, int):
                        quantity = item_data
                        selected_size = None
                        print(f"Creating line item: {product.name}, Size: {selected_size}, Quantity: {quantity}")

                        # Create the OrderLineItem record for a free‑size product
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=selected_size
                        )
                        order_line_item.save()

                    # SIZED PRODUCTS: item_data is a dict mapping size → quantity
                    else:
                        for size, quantity in item_data.items():
                            selected_size = size
                            print(f"Creating line item: {product.name}, Size: {selected_size}, Quantity: {quantity}")

                            # Create one OrderLineItem per size
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=selected_size
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, "Products in your bag wasn't find."
                        "Call us for assistance!"
                    )
                    order.delete()
                    return redirect(reverse('bag'))
            request.session['save_info'] = 'save_info' in request.session.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

        # Otherwise if the form is not valid
        else:
            messages.error(
                request, 'There was an error with your form.'
                'Please double check your information.'
            )

    # Otherwise if the method is not POST
    else:
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

