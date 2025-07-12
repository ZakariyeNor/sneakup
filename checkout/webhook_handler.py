from django.http import HttpResponse


import stripe

class StripeWH_Handler:
    """
    Handle stripe webhooks
    """

    def __init__(self, request):
        self.request = request

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
        
        # Assume that the orde does not exixts
        order_exists = False
        try:
            # Split names 
            name_parts = shipping_details.name.strip().split(' ')
            first_name = name_parts[0]
            last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

            # Get order from the paymentIntent
            order = Order.object.get(
                first_name__iexact=shipping_details.first_name,
                last_name__iexact=shipping_details.last_name,
                email__iexact=shipping_details.email,
                phone_number__iexact=shipping_details.phone,
                street_address_1__iexact=shipping_details.line1,
                street_address_2__iexact=shipping_details.line2,
                postcode__iexact=shipping_details.postal_code,
                city__iexact=shipping_details.city,
                county__iexact=shipping_details.county,
                country__iexact=shipping_details.country,
                grand_total=grand_total,
            )

            # Create order
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in databse',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    first_name=shipping_details.first_name,
                    last_name=shipping_details.last_name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    street_address_1=shipping_details.line1,
                    street_address_2=shipping_details.line2,
                    postcode=shipping_details.postal_code,
                    city=shipping_details.city,
                    county=shipping_details.county,
                    country=shipping_details.country,
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
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500
                )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=400
        )