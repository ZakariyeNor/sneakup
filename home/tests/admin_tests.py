# home/tests/admin_tests.py

import pytest
from django.contrib import admin
from home.models import NewsletterSubscriber
from home.admin import NewsletterSubscriberAdmin


@pytest.mark.django_db
def test_newsletter_admin_registered():
    """Check if the NewsletterSubscriber model
    is registered with its custom admin."""
    assert isinstance(
        admin.site._registry[NewsletterSubscriber],
        NewsletterSubscriberAdmin
    )


def test_newsletter_admin_config():
    """Check list_display, list_filter, and search_fields are set correctly."""
    admin_instance = NewsletterSubscriberAdmin(
            NewsletterSubscriber, admin.site)

    assert admin_instance.list_display == ('email', 'created_at')
    assert admin_instance.list_filter == ('email', 'created_at')
    assert admin_instance.search_fields == ('email', 'created_at')
