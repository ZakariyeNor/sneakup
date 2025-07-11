# This tells Django to use the custom CheckoutConfig class,
# which registers signal handlers in its ready() method.
default_app_config = 'checkout.apps.CheckoutConfig'