import pytest
from decimal import Decimal
from unittest.mock import patch, MagicMock
from bag.context import bag_contents  # adjust import to your project structure
from django.conf import settings

@pytest.fixture(autouse=True)
def set_free_delivery_settings(settings):
    settings.FREE_DELIVERY = Decimal('50.00')
    settings.DELIVERY_PERCENTAGE = Decimal('10')  # 10%
    settings.ESTIMATED_VAT = Decimal('20')  # 20%

@pytest.mark.django_db
@patch('bag.context.get_object_or_404')
def test_bag_contents_free_size_product(mock_get_object_or_404):
    # Setup mock product with price
    mock_product = MagicMock()
    mock_product.price = Decimal('10.00')
    mock_product.name = 'Free Size Product'
    mock_get_object_or_404.return_value = mock_product

    # Mock request with session bag containing free size product with quantity 3
    class Request:
        session = {'bag': {'1': 3}}

    context = bag_contents(Request())

    # Check bag items structure
    assert len(context['bag_items']) == 1
    item = context['bag_items'][0]
    assert item['item_id'] == '1'
    assert item['quantity'] == 3
    assert item['product'] == mock_product
    assert item['selected_size'] is None

    # Check total items and price
    assert context['total_items'] == 3
    assert context['total_price'] == Decimal('30.00')

    # Check delivery cost calculation (30 < 50, so fee applies)
    expected_delivery = (Decimal('30.00') * (settings.DELIVERY_PERCENTAGE / Decimal('100'))).quantize(Decimal('0.01'))
    assert context['delivery_cost'] == expected_delivery

    # Check free delivery amount
    assert context['free_delivery'] == settings.FREE_DELIVERY - Decimal('30.00')

    # Check VAT and grand total calculations
    expected_vat = (Decimal('30.00') * (settings.ESTIMATED_VAT / Decimal('100'))).quantize(Decimal('0.01'))
    expected_grand = (Decimal('30.00') + expected_delivery + expected_vat).quantize(Decimal('0.01'))
    assert context['est_vat'] == expected_vat
    assert context['grand_total'] == expected_grand


@pytest.mark.django_db
@patch('bag.context.get_object_or_404')
def test_bag_contents_sized_product(mock_get_object_or_404):
    # Setup mock product with price
    mock_product = MagicMock()
    mock_product.price = Decimal('20.00')
    mock_product.name = 'Sized Product'
    mock_get_object_or_404.return_value = mock_product

    # Mock request with session bag containing sized product with sizes and quantities
    class Request:
        session = {'bag': {'1': {'S': 2, 'M': 1}}}

    context = bag_contents(Request())

    # Check bag items structure: two sizes
    assert len(context['bag_items']) == 2
    sizes = {item['selected_size'] for item in context['bag_items']}
    assert sizes == {'S', 'M'}

    # Total quantity
    assert context['total_items'] == 3
    # Total price = 3 * 20
    assert context['total_price'] == Decimal('60.00')

    # Delivery should apply as 60 < 50 is false => free delivery
    assert context['delivery_cost'] == Decimal('0.00')
    assert context['free_delivery'] == Decimal('0.00')

    # VAT and grand total checks
    expected_vat = (Decimal('60.00') * (settings.ESTIMATED_VAT / Decimal('100'))).quantize(Decimal('0.01'))
    expected_grand = (Decimal('60.00') + Decimal('0.00') + expected_vat).quantize(Decimal('0.01'))
    assert context['est_vat'] == expected_vat
    assert context['grand_total'] == expected_grand
