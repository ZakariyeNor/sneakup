from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

import stripe
import json
import time
import traceback

class StripeWH_Handler:
    """
    Handle stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {
                'order': order
            }
        )
        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {
                'order': order,
                'contact_email': settings.DEFAULT_EMAIL
            }
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        # Update profile information if save_info was checked
        # Initialize profile as None in case the user is anonymous
        profile = None

        # Extract the username from the PaymentIntent metadata
        username = intent.metadata.name

        # If the user is logged in (not anonymous)
        if username != 'AnonymousUser':
            # Get the user’s profile using the username
            profile = Profile.objects.get(user__username=username)

            # If user want to save the delivery information
            if save_info:
                # Update the user's default shipping information
                # from the PaymentIntent data
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address_1 = shipping_details.address.line1
                profile.default_street_address_2 = shipping_details.address.line2
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_country = shipping_details.address.country
                profile.save()


            
        # Assume that the orde does not exixts
        order_exists = False

        # Delay variable
        attempt = 1
        while attempt <= 5:
            try:
                # Split names 
                name_parts = shipping_details.name.strip().split(' ')
                first_name = name_parts[0]
                last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

                # Get order from the paymentIntent
                order = Order.objects.get(
                    first_name__iexact=first_name,
                    last_name__iexact=last_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    stripe_pid=pid,
                    original_bag=bag,
                )     


                # Create order
                order_exists = True
                break
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in databse',
                    status=200)

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in databse',
                status=200)
        else:
            order = None
            try:
                print("Creating order with:")
                print("Name:", first_name, last_name)
                print("Email:", billing_details.email)
                print("Phone:", shipping_details.phone)
                print("Address:", shipping_details.address)
                print("Bag:", bag)
                print("PID:", pid)
                order = Order.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    country=shipping_details.address.country,
                    stripe_pid=pid,
                    original_bag=bag,
                )
                for item_id, item_data in json.loads(bag).items():

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

            except Exception as e:
                print('Error:', e)
                traceback.print_exc()
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
                )
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=400
        )