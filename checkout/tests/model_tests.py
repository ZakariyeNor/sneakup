import pytest
from decimal import Decimal
from django.conf import settings
from checkout.models import Order, OrderLineItem
from products.models import Product
from profiles.models import Profile


@pytest.mark.django_db
def test_order_string_representation():
    order = Order.objects.create(
        first_name="Jane",
        last_name="Doe",
        email="jane@example.com",
        phone_number="1234567890",
        country="SE",
        city="Stockholm",
        street_address_1="Test Street 1"
    )
    assert str(order).startswith("Order #")
    assert f"{order.first_name} {order.last_name}" in str(order)


@pytest.mark.django_db
def test_order_number_generated():
    order = Order.objects.create(
        first_name="John",
        last_name="Smith",
        email="john@example.com",
        phone_number="1234567890",
        country="SE",
        city="Stockholm",
        street_address_1="Main Street 1"
    )
    assert order.order_number is not None
    assert len(str(order.order_number)) >= 15


@pytest.mark.django_db
def test_update_total_calculates_correctly(settings):
    product = Product.objects.create(
            name="Shoe", sku="1234", price=Decimal("100.00"))
    order = Order.objects.create(
        first_name="Anna",
        last_name="Smith",
        email="anna@example.com",
        phone_number="1234567890",
        country="SE",
        city="Stockholm",
        street_address_1="Street 1"
    )
    line = OrderLineItem.objects.create(
            order=order, product=product, quantity=2)
    order.update_total()

    expected_order_total = Decimal("200.00")
    vat = (expected_order_total * Decimal(str(
        settings.ESTIMATED_VAT)) / Decimal("100")).quantize(Decimal("0.01"))
    if expected_order_total < settings.FREE_DELIVERY:
        delivery = (
            expected_order_total * settings.DELIVERY_PERCENTAGE / Decimal(
                "100")).quantize(Decimal("0.01"))
    else:
        delivery = Decimal("0.00")
    grand_total = (
        expected_order_total + vat + delivery).quantize(Decimal("0.01"))

    assert order.order_total == expected_order_total
    assert order.vat == vat
    assert order.delivery == delivery
    assert order.grand_total == grand_total


@pytest.mark.django_db
def test_lineitem_total_calculated_correctly():
    product = Product.objects.create(
        name="Hat", sku="9999", price=Decimal("25.00"))
    order = Order.objects.create(
        first_name="Eva",
        last_name="Test",
        email="eva@example.com",
        phone_number="9876543210",
        country="SE",
        city="Gothenburg",
        street_address_1="Street 2"
    )
    lineitem = OrderLineItem.objects.create(
        order=order, product=product, quantity=3)
    assert lineitem.lineitem_total == Decimal("75.00")
