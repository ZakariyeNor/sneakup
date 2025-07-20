import pytest
from django.urls import reverse, resolve
from checkout import views
from checkout.webhooks import webhook

@pytest.mark.django_db
class TestCheckoutUrls:

    def test_checkout_url_resolves(self):
        path = reverse('checkout')
        assert resolve(path).func == views.checkout

    def test_checkout_success_url_resolves(self):
        order_number = 'ABC123'
        path = reverse('checkout_success', args=[order_number])
        resolved = resolve(path)
        assert resolved.func == views.checkout_success
        assert resolved.kwargs['order_number'] == order_number

    def test_cache_checkout_data_url_resolves(self):
        path = reverse('cache_checkout_data')
        assert resolve(path).func == views.cache_checkout_data

    def test_webhook_url_resolves(self):
        path = reverse('webhook')
        assert resolve(path).func == webhook


@pytest.mark.django_db
class TestCheckoutUrlsHttp:

    def test_checkout_get(self, client):
        url = reverse('checkout')
        response = client.get(url)
        # Expect 200 or redirect if no bag (depends on your logic)
        assert response.status_code in (200, 302)

    def test_cache_checkout_data_post(self, client):
        url = reverse('cache_checkout_data')
        response = client.post(url, data={'client_secret': 'pi_test_secret'})
        # Since no session or user, may fail or 400, just check for response
        assert response.status_code in (200, 400)

