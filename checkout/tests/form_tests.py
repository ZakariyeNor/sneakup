import pytest
from checkout.forms import OrderForm

@pytest.mark.django_db
class TestOrderForm:

    def valid_form_data(self):
        return {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'phone_number': '1234567890',
            'street_address_1': '123 Main St',
            'street_address_2': '',
            'city': 'Townsville',
            'postcode': '12345',
            'country': 'SE',
            'county': 'Some County',
        }

    def test_form_valid_with_correct_data(self):
        form = OrderForm(data=self.valid_form_data())
        assert form.is_valid()

    def test_form_invalid_missing_required_fields(self):
        data = self.valid_form_data()
        data['first_name'] = ''  # required field empty
        data['email'] = ''
        form = OrderForm(data=data)
        assert not form.is_valid()
        assert 'first_name' in form.errors
        assert 'email' in form.errors

    def test_form_invalid_email_format(self):
        data = self.valid_form_data()
        data['email'] = 'invalid-email'
        form = OrderForm(data=data)
        assert not form.is_valid()
        assert 'email' in form.errors
        assert 'Please enter a valid email address.' in form.errors['email']

    def test_form_max_length_exceeded(self):
        data = self.valid_form_data()
        data['first_name'] = 'A' * 256  # Exceed max_length
        data['street_address_1'] = 'B' * 256
        form = OrderForm(data=data)
        assert not form.is_valid()
        assert 'first_name' in form.errors
        assert 'street_address_1' in form.errors


