from django.contrib import admin
from .models import PrivacyPolicy

# Register privacy policy on the admin
@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    """
    Give ability to search and filter
    """
    ordering = (
        '-updated_at',
    )
    list_display = (
        'title', 'created_at',
    )

    search_fields = (
        'title', 'created_at', 'updated_at',
    )
    list_filter = (
        'title', 'created_at', 'updated_at',
    )