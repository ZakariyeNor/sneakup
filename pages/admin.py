from django.contrib import admin
from .models import (
    PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage,
    AboutPageHero, OurMission, NewArrivals, OurMaterials,
    BestSelling, LaunchedProducts,
)

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


# Register AboutPageHero model
@admin.register(AboutPageHero)
class AboutPageHeroAdmin(admin.ModelAdmin):
    list_display = ('overlay_title', 'hero_image')

# Register OurMission model
@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
    list_display = ('our_mission_title',)

# Register NewArrivals model
@admin.register(NewArrivals)
class NewArrivalsAdmin(admin.ModelAdmin):
    list_display = ('new_name', 'launched_date')

# Register OurMaterials model
@admin.register(OurMaterials)
class OurMaterialsAdmin(admin.ModelAdmin):
    list_display = ('our_materials_title',)

# Register BestSelling model
@admin.register(BestSelling)
class BestSellingAdmin(admin.ModelAdmin):
    list_display = ('best_selling_title',)

# Register LaunchedProducts model
@admin.register(LaunchedProducts)
class LaunchedProductsAdmin(admin.ModelAdmin):
    list_display = ('launched_name', 'launched_date')