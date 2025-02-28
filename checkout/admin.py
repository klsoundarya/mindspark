from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """Defines inline display for Order Line Items within an Order in the admin panel."""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for managing orders."""
    inlines = (OrderLineItemAdminInline,)
    # Fields that should be read-only in the admin panel
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',  'original_cart',
                       'stripe_pid')
    # Fields displayed in the order detail view
    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_cart',
                       'stripe_pid')
    # Fields displayed in the order list view
    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)
    # Orders are displayed in descending order by date
    ordering = ('-date',)

# Register the Order model with the custom admin configuration
admin.site.register(Order, OrderAdmin)
