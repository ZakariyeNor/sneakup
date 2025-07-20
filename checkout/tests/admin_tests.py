from django.test import TestCase
from django.contrib.admin.sites import site
from checkout.models import Order, OrderLineItem
from checkout.admin import OrderAdmin, OrderLineItemAdminInline

class TestOrderAdminRegistration(TestCase):

    def test_order_model_registered_with_custom_admin(self):
        self.assertIn(Order, site._registry)
        self.assertIsInstance(site._registry[Order], OrderAdmin)

    def test_order_admin_readonly_fields(self):
        admin_instance = OrderAdmin(Order, site)
        expected = {
            'order_number', 'first_name', 'last_name', 'date',
            'delivery', 'order_total', 'grand_total',
            'original_bag', 'stripe_pid'
        }
        self.assertTrue(set(admin_instance.readonly_fields).issuperset(expected))

    def test_order_admin_list_display(self):
        admin_instance = OrderAdmin(Order, site)
        expected = ('order_number', 'email', 'postcode', 'date')
        self.assertEqual(admin_instance.list_display, expected)

    def test_order_admin_list_filter(self):
        admin_instance = OrderAdmin(Order, site)
        expected = ('date', 'country', 'city', 'postcode')
        self.assertEqual(admin_instance.list_filter, expected)

    def test_order_admin_search_fields(self):
        admin_instance = OrderAdmin(Order, site)
        expected = (
            'order_number', 'first_name', 'last_name',
            'email', 'phone_number', 'postcode',
            'city', 'street_address_1'
        )
        self.assertEqual(admin_instance.search_fields, expected)

    def test_order_admin_inline_is_orderlineitem(self):
        admin_instance = OrderAdmin(Order, site)
        self.assertIn(OrderLineItemAdminInline, admin_instance.inlines)

    def test_inline_admin_readonly_fields(self):
        inline = OrderLineItemAdminInline(OrderLineItem, site)
        self.assertEqual(inline.readonly_fields, ('lineitem_total',))
