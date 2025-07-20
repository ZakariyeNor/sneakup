# home/tests/model_tests.py

import pytest
from django.db import IntegrityError
from home.models import NewsletterSubscriber
from django.utils.timezone import now

@pytest.mark.django_db
def test_create_newsletter_subscriber():
    subscriber = NewsletterSubscriber.objects.create(email="test@example.com")
    assert subscriber.email == "test@example.com"
    assert subscriber.created_at is not None

@pytest.mark.django_db
def test_newsletter_email_uniqueness():
    NewsletterSubscriber.objects.create(email="unique@example.com")
    with pytest.raises(IntegrityError):
        NewsletterSubscriber.objects.create(email="unique@example.com")

@pytest.mark.django_db
def test_newsletter_str_method():
    subscriber = NewsletterSubscriber.objects.create(email="hello@domain.com")
    expected_str = f'hello@domain.com | subscribed on {subscriber.created_at.strftime("%Y-%m-%d")}'
    assert str(subscriber) == expected_str
