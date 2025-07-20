# home/tests/url_tests.py

import pytest
from django.urls import reverse, resolve
from home import views

@pytest.mark.django_db
def test_home_url_resolves():
    path = reverse('home')
    assert resolve(path).func == views.index

@pytest.mark.django_db
def test_email_subscribe_url_resolves():
    path = reverse('email_subscribe')
    assert resolve(path).func == views.email_subscribe
