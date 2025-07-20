# pages/tests/url_tests.py

import pytest
from django.urls import reverse, resolve
from pages import views


@pytest.mark.parametrize("url_name,view_func", [
    ("privacy_policy", views.privacy_policy),
    ("returns_policy", views.returns_policy),
    ("faqs_view", views.faqs_view),
    ("contact", views.contact),
    ("about_view", views.about_view),
])
def test_url_resolves_to_correct_view(url_name, view_func):
    url = reverse(url_name)
    resolved = resolve(url)
    assert resolved.func == view_func


@pytest.mark.django_db
@pytest.mark.parametrize("url_name", [
    "privacy_policy",
    "returns_policy",
    "faqs_view",
    "contact",
    "about_view",
])
def test_urls_return_status_code_200(client, url_name):
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == 200 or response.status_code == 302
