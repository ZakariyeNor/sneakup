import pytest
import uuid
from unittest.mock import patch
from checkout.models import Order, OrderLineItem
from products.models import Product

@pytest.mark.django_db
class TestOrderLineItemSignals:

    @pytest.fixture
    def product(self, django_db_blocker):
        with django_db_blocker.unblock():
            return Product.objects.create(name='Test Product', price=10, sku='SKU123')

    @pytest.fixture
    def order(self, django_db_blocker):
        with django_db_blocker.unblock():
            return Order.objects.create(
                first_name='John',
                last_name='Doe',
                email='john@example.com',
                phone_number='1234567890',
                country='SE',
                city='Townsville',
                street_address_1='123 Main St',
                order_number=str(uuid.uuid4()),  # Use valid UUID string here
            )

    def test_post_save_calls_update_total(self, order, product):
        line_item = OrderLineItem(order=order, product=product, quantity=1)
        with patch.object(Order, 'update_total') as mock_update_total:
            line_item.save()
            mock_update_total.assert_called_once()

    def test_post_delete_calls_update_total(self, order, product):
        line_item = OrderLineItem.objects.create(order=order, product=product, quantity=1)
        with patch.object(Order, 'update_total') as mock_update_total:
            line_item.delete()
            mock_update_total.assert_called_once()
