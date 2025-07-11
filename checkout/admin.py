from django.contrib import admin
from .models import Order, OrderLineItem



# Inline admin for order line
class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline admin configuration for displaying order line items 
    within the Order admin detail view.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    

# Register Order with the admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        'order_number', 'first_name',
        'last_name', 'date', 'delivery',
        'order_total', 'grand_total',
    )

    list_display = (
        'order_number',
        'email',
        'postcode',
        'date',
    )

    list_filter = (
        'date', 'country', 'city', 
        'postcode',
    )
    search_fields = (
        'order_number',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'postcode',
        'city',
        'street_address_1',
    )
    fields = (
        'order_number',
        'first_name',
        'last_name',
        'date',
        'email',
        'phone_number',
        'country',
        'postcode',
        'city',
        'street_address_1',
        'street_address_2',
        'county',
        'delivery',
        'order_total',
        'vat',
        'grand_total',
    )
    ordering = ('-date',)
