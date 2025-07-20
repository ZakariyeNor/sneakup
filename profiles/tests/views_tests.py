import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from checkout.models import Order


@pytest.mark.django_db
def test_profile_view_authenticated(client):
    user = User.objects.create_user(username='testuser', password='password123')
    client.login(username='testuser', password='password123')
    profile, _ = Profile.objects.get_or_create(user=user)

    response = client.get(reverse('profile'))
    assert response.status_code == 200
    assert b'Your profile' in response.content or b'orders' in response.content


@pytest.mark.django_db
def test_order_detail_view_authenticated(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')

    profile, _ = Profile.objects.get_or_create(user=user)

    order = Order.objects.create(
        profile=profile,
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        phone_number='123456789',
        country='SE',
        postcode='12345',
        city='Stockholm',
        street_address_1='Main Street 1',
        street_address_2='',
        county='Stockholm',
        original_bag='{}',
        stripe_pid='teststripepid'
    )

    url = reverse('order_detail', args=[order.order_number])
    response = client.get(url)

    assert response.status_code == 200
    assert b'confirmation summary for order' in response.content
