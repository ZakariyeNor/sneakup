import pytest
from django.contrib import admin
from products.admin import ProductAdmin, CaregoryAdmin
from products.models import Product, Category

def test_product_model_registered():
    assert admin.site.is_registered(Product)

def test_category_model_registered():
    assert admin.site.is_registered(Category)

def test_product_admin_configuration():
    model_admin = admin.site._registry[Product]
    assert isinstance(model_admin, ProductAdmin)
    
    assert model_admin.list_display == ('sku', 'name', 'category', 'price', 'rating', 'image')
    assert model_admin.list_filter == ('category',)
    assert model_admin.search_fields == ('category',)
    assert model_admin.ordering == ('sku', 'name', 'category')

def test_category_admin_configuration():
    model_admin = admin.site._registry[Category]
    assert isinstance(model_admin, CaregoryAdmin)
    
    assert model_admin.list_display == ('friendly_name', 'name')
    assert model_admin.list_filter == ('friendly_name',)
    assert model_admin.search_fields == ('name',)
