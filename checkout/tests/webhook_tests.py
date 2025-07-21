import pytest
from django.test import RequestFactory
from django.http import HttpResponse
from unittest.mock import patch, MagicMock
from checkout import webhook


class TestWebhookView:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.factory = RequestFactory()
        self.url = '/webhook/'

    def test_missing_signature_header(self):
        request = self.factory.post(
            self.url, data=b'{}', content_type='application/json')
        # No 'HTTP_STRIPE_SIGNATURE' in META
        response = webhook.webhook(request)
        assert response.status_code == 400
        assert response.content == b"Missing Stripe Signature"

    @patch('checkout.webhook.stripe.Webhook.construct_event')
    def test_invalid_payload_raises_value_error(self, mock_construct_event):
        mock_construct_event.side_effect = ValueError("Invalid payload")
        request = self.factory.post(
            self.url, data=b'invalid', content_type='application/json',
            HTTP_STRIPE_SIGNATURE='sig')
        response = webhook.webhook(request)
        assert response.status_code == 400

    @patch('checkout.webhook.stripe.Webhook.construct_event')
    def test_invalid_signature_raises_signature_verification_error(
            self, mock_construct_event):
        from stripe.error import SignatureVerificationError
        mock_construct_event.side_effect = SignatureVerificationError(
                "Invalid signature", 'sig')
        request = self.factory.post(
                self.url, data=b'{}', content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig')
        response = webhook.webhook(request)
        assert response.status_code == 400

    @patch('checkout.webhook.stripe.Webhook.construct_event')
    def test_generic_exception_returns_400(self, mock_construct_event):
        mock_construct_event.side_effect = Exception("Other error")
        request = self.factory.post(
                self.url, data=b'{}', content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig')
        response = webhook.webhook(request)
        assert response.status_code == 400
        assert b"Other error" in response.content

    @patch('checkout.webhook.stripe.Webhook.construct_event')
    @patch('checkout.webhook.StripeWH_Handler')
    def test_valid_event_calls_correct_handler(
            self, mock_handler_class, mock_construct_event):
        # Prepare mock event
        event = {'type': 'payment_intent.succeeded'}
        mock_construct_event.return_value = event

        # Prepare mock handler instance
        mock_handler = MagicMock()
        mock_handler.handle_payment_intent_succeeded.return_value = HttpResponse(
            'Success', status=200)
        mock_handler.handle_event.return_value = HttpResponse(
                'Generic event', status=200)
        mock_handler_class.return_value = mock_handler

        request = self.factory.post(
                self.url, data=b'{}', content_type='application/json',
                HTTP_STRIPE_SIGNATURE='sig')

        # Test known event type calls correct handler method
        response = webhook.webhook(request)
        mock_handler.handle_payment_intent_succeeded.assert_called_once_with(
            event)
        assert response.status_code == 200
        assert response.content == b'Success'

        # Change event type to unknown
        mock_construct_event.return_value = {'type': 'unknown.event'}
        mock_handler.handle_event.return_value = HttpResponse(
            'Handled generic', status=200)

        response = webhook.webhook(request)
        mock_handler.handle_event.assert_called_with({'type': 'unknown.event'})
        assert response.status_code == 200
        assert response.content == b'Handled generic'
