from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderLineItem
from products.models import Product
from django.contrib import messages
from .forms import OrderForm
from profiles.models import Profile
from profiles.forms import ProfileForm
from django.conf import settings

# Get bag contents from the context file in bag app
from bag.context import bag_contents

# Import json
import stripe

# Import stripe
import json


@require_POST
@csrf_exempt
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'name': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now. Please try again later.'
        )
        return HttpResponse(content=e, status=400)


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
            'first_name': request.POST.get('first_name', '').strip(),
            'last_name': request.POST.get('last_name', '').strip(),
            'email': request.POST.get('email', '').strip(),
            'phone_number': request.POST.get('phone_number', '').strip(),
            'street_address_1': request.POST.get('street_address_1', '').strip(),
            'street_address_2': request.POST.get('street_address_2', '').strip(),
            'city': request.POST.get('city', '').strip(),
            'postcode': request.POST.get('postcode', '').strip(),
            'county': request.POST.get('county', '').strip(),
            'country': request.POST.get('country', '').strip(),
        }
        # Bind the submitted form data to an
        # OrderForm instance for validation
        order_form = OrderForm(form_data)

        # Check if the form is valid and save if it's
        if order_form.is_valid():
            order = order_form.save(commit=False)

            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            
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
            request.session['save_info'] = 'save_info' in request.POST
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

        # Check if the user is logged in to use the user's
        # default delivery information in their profile page
        # to pre-fill the form on the checkout page
        if request.user.is_authenticated:
            # get their email, first name and
            # last name from the Django User model
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.user.first_name or '',
                    'last_name': profile.user.last_name or '',
                    'email': profile.user.email,
                    # Get the rest from the default delivery information
                    'phone_number': profile.default_phone_number,
                    'street_address_1': profile.default_street_address_1,
                    'street_address_2': profile.default_street_address_2,
                    'city': profile.default_city,
                    'postcode': profile.default_postcode ,
                    'county': profile.default_county,
                })
            # If the user's profile does not exist,
            # skip pre-filling the form and continue with
            # a blank order form instead
            except Profile.DoesNotExist:
                order_form = OrderForm()
        # Otherwise if user is not logged in
        else:
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


# Checkout_success view
def checkout_success(request, order_number):
    """
    Handle successful checkouts.

    This view is triggered after a successful payment and completed checkout process.
    It retrieves the order using the provided order number, clears the shopping bag from
    the session, and displays a success message to the user along with order details.
    """

    # Check if save_info checkbox is checked
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Check if the user is logged in.
    # Then attach user's profile to the order
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        order.profile = profile
        order.save()

        # Then save the user's information
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
                'default_city': order.city,
                'default_postcode': order.postcode,
                'default_county': order.county, 
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
            else:
                messages.error(
                    request,
                    f'Form is not valid, Please double check the form.'
                )

    
    messages.success(
                request,
                f'Order successfully processed!. Your order number is {order_number}.'
                f'A confirmation email will be sent to {order.email}.'
    )

    # Delete the bag from the session
    if 'bag' in request.session:
        del request.session['bag']
        
    order_form = OrderForm(instance=order)
    return render(
        request,
        template_name= 'checkout/checkout_success.html',
        context = {
            'order': order,
            'order_form': order_form,
            'from_profile': False,
        }
    )
