from django.contrib import admin
from .models import PrivacyPolicy, ReturnsPolicy

# Register privacy policy on the admin
@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    """
    Give ability to search and filter the uploaded
    pdf privacy policies. 
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

# Register returns policy on the admin
@admin.register(ReturnsPolicy)
class ReturnsPolicyAdmin(admin.ModelAdmin):
    """
    Give ability to search and filter the uploaded
    pdf returns policies. 
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