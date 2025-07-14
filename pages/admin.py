from django.contrib import admin
from .models import PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage

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


# Register FAQs model on the admin
@admin.register(FAQs)
class FAQsAdmin(admin.ModelAdmin):
    """
    Admin model for FAQs: enable search and filter
    by question and creation date.
    """

    ordering = (
        '-created_at',
    )
    list_display = (
        'id', 'created_at',
    )
    search_fields = (
        'question',
    )
    list_filter = (
        'created_at',
    )



# Register Contact model on the admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin model for FAQs: enable search and filter
    by question and creation date.
    """
    ordering = (
        '-created_at',
    )
    list_display = (
        'full_name', 'created_at', 
    )

    search_fields = (
        'id', 'fullname', 'email',
    )
    list_filter = (
        'created_at', 'id', 'full_name', 'email',
    )
    
    readonly_fields = (
        'full_name', 'email', 'order_number',
        'message', 'send_info', 'created_at',
    )
