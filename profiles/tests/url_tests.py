import pytest
from django.urls import reverse, resolve
from profiles import views


def test_profile_url_resolves():
    url = reverse('profile')
    resolver = resolve(url)
    assert resolver.view_name == 'profile'
    assert resolver.func == views.profile


def test_order_detail_url_resolves():
    # Use a dummy order_number as URL parameter
    url = reverse('order_detail', args=['dummy-order-number'])
    resolver = resolve(url)
    assert resolver.view_name == 'order_detail'
    assert resolver.func == views.order_detail


@pytest.mark.django_db
def test_profile_url_status_code(client):
    # Without login, profile page should redirect (302)
    url = reverse('profile')
    response = client.get(url)
    assert response.status_code in (301, 302)


@pytest.mark.django_db
def test_order_detail_url_status_code_requires_login(client):
    url = reverse('order_detail', args=['dummy-order-number'])
    response = client.get(url)
    # Not logged in → redirect to login page
    assert response.status_code in (301, 302)
