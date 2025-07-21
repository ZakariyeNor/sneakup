import json
import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import RequestFactory
from unittest.mock import patch, MagicMock
from checkout.views import cache_checkout_data
from checkout.models import Order
from profiles.models import Profile


@pytest.mark.django_db
class TestCacheCheckoutDataView:

    @patch('checkout.views.stripe.PaymentIntent.modify')
    def test_cache_checkout_data_success(self, mock_modify):
        factory = RequestFactory()
        request = factory.post('/cache_checkout_data/', data={
            'client_secret': 'pi_123_secret_abc',
            'save_info': 'true',
        })
        request.session = {'bag': {'1': 2}}
        request.user = User(username='testuser')

        response = cache_checkout_data(request)
        assert response.status_code == 200
        mock_modify.assert_called_once()

    @patch('checkout.views.stripe.PaymentIntent.modify', side_effect=Exception(
        'Stripe error'))
    def test_cache_checkout_data_failure(self, mock_modify):
        factory = RequestFactory()
        request = factory.post('/cache_checkout_data/', data={
            'client_secret': 'pi_123_secret_abc',
            'save_info': 'true',
        })
        request.session = {'bag': {'1': 2}}
        request._messages = MagicMock()
        request.user = User(username='testuser')

        response = cache_checkout_data(request)
        assert response.status_code == 400


@pytest.mark.django_db
class TestCheckoutView:

    @pytest.fixture
    def product(self, django_db_blocker):
        with django_db_blocker.unblock():
            from products.models import Product
            return Product.objects.create(
                name='Test Product', price=10, sku='SKU123')

    @patch('checkout.views.bag_contents')
    @patch('checkout.views.stripe.PaymentIntent.create')
    def test_get_checkout_with_empty_bag_redirects(
            self, mock_payment_intent, mock_bag_contents, client):
        session = client.session
        session['bag'] = {}
        session.save()

        response = client.get(reverse('checkout'))
        messages = list(get_messages(response.wsgi_request))
        assert response.status_code == 302
        assert response.url == reverse('products')
        assert any("nothing in your bag" in str(m) for m in messages)

    @pytest.mark.django_db
    def test_post_checkout_valid_form_creates_order_and_redirects(
            self, client, product):
        # Add product to bag in session
        bag = {str(product.id): 3}
        session = client.session
        session['bag'] = bag
        session.save()

        post_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address_1': '123 Main St',
            'street_address_2': '',
            'city': 'Townsville',
            'postcode': '12345',
            'county': '',
            'country': 'SE',
            'client_secret': 'pi_abc_secret_xyz',
        }

        response = client.post(reverse('checkout'), data=post_data)
        assert response.status_code == 302
        order = Order.objects.first()
        assert order is not None
        assert response.url == reverse(
            'checkout_success', args=[order.order_number])


@pytest.mark.django_db
class TestCheckoutSuccessView:

    @pytest.fixture
    def user(self, django_db_blocker):
        with django_db_blocker.unblock():
            return User.objects.create_user(username='user1', password='pass')

    @pytest.fixture
    def profile(self, user, django_db_blocker):
        with django_db_blocker.unblock():
            return Profile.objects.create(user=user)

    @pytest.fixture
    def order(self, profile, django_db_blocker):
        with django_db_blocker.unblock():
            return Order.objects.create(
                first_name='John',
                last_name='Doe',
                email='john@example.com',
                phone_number='1234567890',
                country='SE',
                city='Townsville',
                street_address_1='123 Main St',
                order_number='1234567890abcdef',
                profile=profile,
            )
