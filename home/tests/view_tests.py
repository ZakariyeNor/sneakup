# home/tests/view_tests.py

import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product, Category
from home.models import NewsletterSubscriber


@pytest.mark.django_db
def test_index_view_with_products_and_categories(client):
    # Create dummy categories and products
    category = Category.objects.create(name='shoes', friendly_name='Shoes')
    Product.objects.create(name='Test Product', price=10.0, category=category)

    response = client.get(reverse('home'))
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert "Welcome to DUAC!" in str(messages[0])
    assert b"Lanezra" in response.content


@pytest.mark.django_db
def test_index_view_no_products(client):
    # No products or categories created
    response = client.get(reverse('home'))
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert "no categories available" in str(messages[0]).lower()


@pytest.mark.django_db
def test_email_subscribe_post_valid_email(client):
    data = {"email": "test@example.com"}
    response = client.post(reverse('email_subscribe'), data, follow=True)
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert NewsletterSubscriber.objects.filter(
            email="test@example.com").exists()
    assert "Thanks for subscribing!" in str(messages[0])


@pytest.mark.django_db
def test_email_subscribe_duplicate_email(client):
    NewsletterSubscriber.objects.create(email="test@example.com")
    data = {"email": "test@example.com"}

    response = client.post(reverse('email_subscribe'), data, follow=True)
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert "already subscribed" in str(messages[0])


@pytest.mark.django_db
def test_email_subscribe_invalid_email(client):
    data = {"email": "invalid-email"}
    response = client.post(reverse('email_subscribe'), data, follow=True)
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert "valid email address" in str(messages[0])


@pytest.mark.django_db
def test_email_subscribe_empty_email(client):
    data = {"email": ""}
    response = client.post(reverse('email_subscribe'), data, follow=True)
    messages = list(get_messages(response.wsgi_request))

    assert response.status_code == 200
    assert "cannot be empty" in str(messages[0])
