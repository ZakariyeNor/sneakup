from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'


    def ready(self):
        """
        Override the ready method to ensure that signals are
        connected when the app is initialized.
        """
        # Import signal handlers to ensure they're
        # registered when the app is ready
        import checkout.signals