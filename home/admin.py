from django.contrib import admin
from .models import NewsletterSubscriber

# Register email subscription model
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    """
    Give ability to search emails wnad when they've been created at
    """
    list_display = (
        'email', 'created_at',
    )

    
    list_filter = (
        'email', 'created_at',
    )

    search_fields = (
        'email', 'created_at',
    )


