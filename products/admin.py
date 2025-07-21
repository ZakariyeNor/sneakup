from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
# Product admin
class ProductAdmin(admin.ModelAdmin):
    """
    Customize how the data properties look like on the admin page
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    list_filter = (
        'category',
    )

    search_fields = (
        'category',
    )
    ordering = (
        'sku',
        'name',
        'category',
    )


@admin.register(Category)
# Caregory admin
class CaregoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    list_filter = (
        'friendly_name',
    )

    search_fields = (
        'name',
    )
