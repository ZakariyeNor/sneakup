import logging
logger = logging.getLogger(__name__)
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
        print(f"Sending email to: {cust_email}")
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
                'contact_email': settings.DEFAULT_FROM_EMAIL
            }
        )
        print("EMAIL SUBJECT:", subject)
        print("EMAIL BODY:", body)
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
        Handle the payment_intent.succeeded webhook from Stripe.
        """

        intent = event.data.object
        pid = intent.id

        # Safely get bag metadata
        bag = json.loads(intent.metadata.get('bag', '{}')) if intent.metadata else {}

        save_info = getattr(intent.metadata, 'save_info', False)
        username = getattr(intent.metadata, 'name', 'AnonymousUser')

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean shipping address
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Initialize profile if user is logged in
        profile = None
        if username != 'AnonymousUser':
            try:
                profile = Profile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_street_address_1 = shipping_details.address.line1
                    profile.default_street_address_2 = shipping_details.address.line2
                    profile.default_postcode = shipping_details.address.postal_code
                    profile.default_city = shipping_details.address.city
                    profile.default_county = shipping_details.address.state
                    profile.default_country = shipping_details.address.country
                    profile.save()
            except Profile.DoesNotExist:
                pass

        # Extract first and last name from shipping details
        name_parts = shipping_details.name.strip().split(' ')
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

        # Check if order exists
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
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
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            try:
                self._send_confirmation_email(order)
            except Exception as e:
                logger.exception(f"Error sending confirmation email for existing order: {e}")
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200
            )

        # If order does not exist, create it
        order = None
        try:
            email = billing_details.email or getattr(intent.metadata, 'email', None)
            if not email:
                email = 'no-email@example.com'
            order = Order.objects.create(
                first_name=first_name,
                last_name=last_name,
                profile=profile,
                email=email,
                phone_number=shipping_details.phone or "0000000000",
                street_address_1=shipping_details.address.line1,
                street_address_2=shipping_details.address.line2,
                postcode=shipping_details.address.postal_code,
                city=shipping_details.address.city,
                county=shipping_details.address.state,
                country=shipping_details.address.country,
                stripe_pid=pid,
                original_bag=bag,
            )

            # Create OrderLineItems
            for item_id, item_data in bag.items():
                product = get_object_or_404(Product, pk=item_id)

                if isinstance(item_data, int):
                    # Free-size product
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                        product_size=None
                    )
                    order_line_item.save()
                else:
                    # Sized product
                    for size, quantity in item_data.items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size
                        )
                        order_line_item.save()

        except Exception as e:
            logger.exception(f"Error creating order from webhook: {e}")
            if order:
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500
            )

        # Send confirmation email (safe)
        try:
            self._send_confirmation_email(order)
        except Exception as e:
            logger.exception(f"Error sending confirmation email for new order: {e}")

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
