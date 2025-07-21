import pytest
from django.contrib import admin
from pages import admin as pages_admin
from pages.models import (
    PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage,
    AboutPageHero, OurMission, NewArrivals, OurMaterials,
    BestSelling, LaunchedProducts,
)


@pytest.mark.django_db
def test_privacy_policy_admin_registration():
    model_admin = admin.site._registry.get(PrivacyPolicy)
    assert model_admin is not None
    assert model_admin.ordering == ('-updated_at',)
    assert 'title' in model_admin.list_display
    assert 'created_at' in model_admin.list_display
    assert 'title' in model_admin.search_fields
    assert 'created_at' in model_admin.search_fields
    assert 'updated_at' in model_admin.search_fields
    assert 'title' in model_admin.list_filter
    assert 'created_at' in model_admin.list_filter
    assert 'updated_at' in model_admin.list_filter


@pytest.mark.django_db
def test_returns_policy_admin_registration():
    model_admin = admin.site._registry.get(ReturnsPolicy)
    assert model_admin is not None
    assert model_admin.ordering == ('-updated_at',)
    assert 'title' in model_admin.list_display
    assert 'created_at' in model_admin.list_display
    assert 'title' in model_admin.search_fields
    assert 'created_at' in model_admin.search_fields
    assert 'updated_at' in model_admin.search_fields
    assert 'title' in model_admin.list_filter
    assert 'created_at' in model_admin.list_filter
    assert 'updated_at' in model_admin.list_filter


@pytest.mark.django_db
def test_faqs_admin_registration():
    model_admin = admin.site._registry.get(FAQs)
    assert model_admin is not None
    assert model_admin.ordering == ('-created_at',)
    assert 'id' in model_admin.list_display
    assert 'created_at' in model_admin.list_display
    assert 'question' in model_admin.search_fields
    assert 'created_at' in model_admin.list_filter


@pytest.mark.django_db
def test_contact_message_admin_registration():
    model_admin = admin.site._registry.get(ContactMessage)
    assert model_admin is not None
    assert model_admin.ordering == ('-created_at',)
    assert 'full_name' in model_admin.list_display
    assert 'created_at' in model_admin.list_display
    assert 'id' in model_admin.search_fields
    assert 'email' in model_admin.search_fields or 'email' in getattr(
        model_admin, 'search_fields', ())
    assert 'full_name' in model_admin.list_filter
    assert 'email' in model_admin.list_filter
    # Check readonly_fields includes expected fields
    readonly = getattr(model_admin, 'readonly_fields', ())
    for field in (
        'full_name', 'email', 'order_number',
        'message', 'send_info', 'created_at'
    ):
        assert field in readonly


@pytest.mark.django_db
def test_about_page_hero_admin_registration():
    model_admin = admin.site._registry.get(AboutPageHero)
    assert model_admin is not None
    assert 'overlay_title' in model_admin.list_display
    assert 'hero_image' in model_admin.list_display


@pytest.mark.django_db
def test_our_mission_admin_registration():
    model_admin = admin.site._registry.get(OurMission)
    assert model_admin is not None
    assert 'our_mission_title' in model_admin.list_display


@pytest.mark.django_db
def test_new_arrivals_admin_registration():
    model_admin = admin.site._registry.get(NewArrivals)
    assert model_admin is not None
    assert 'new_name' in model_admin.list_display
    assert 'launched_date' in model_admin.list_display


@pytest.mark.django_db
def test_our_materials_admin_registration():
    model_admin = admin.site._registry.get(OurMaterials)
    assert model_admin is not None
    assert 'our_materials_title' in model_admin.list_display


@pytest.mark.django_db
def test_best_selling_admin_registration():
    model_admin = admin.site._registry.get(BestSelling)
    assert model_admin is not None
    assert 'best_selling_title' in model_admin.list_display


@pytest.mark.django_db
def test_launched_products_admin_registration():
    model_admin = admin.site._registry.get(LaunchedProducts)
    assert model_admin is not None
    assert 'launched_name' in model_admin.list_display
    assert 'launched_date' in model_admin.list_display
