from django import forms
from .models import Order

#Order Form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Form fields
        fields = (
            'first_name', 'last_name', 'email',
            'phone_number', 'street_address_1', 'street_address_2',
            'city', 'postcode', 'country', 'county',
        )

        # Custom error messages
        error_messages = {
                'first_name': {
                    'required': 'Please enter your first name.',
                    'max_length': 'First name is too long.',
                },
                'last_name': {
                    'required': 'Please enter your last name.',
                    'max_length': 'Last name is too long.',
                },
                'email': {
                    'required': 'Please enter your email address.',
                    'invalid': 'Please enter a valid email address.',
                },
                'phone_number': {
                    'required': 'Please enter your phone number.',
                    'invalid': 'Please enter a valid phone number.',
                },
                'street_address_1': {
                    'required': 'Please enter your street address.',
                    'max_length': 'Street address is too long.',
                },
                'street_address_2': {
                    'max_length': 'Street address 2 is too long.',
                },
                'city': {
                    'required': 'Please enter your city.',
                    'max_length': 'City name is too long.',
                },
                'postcode': {
                    'required': 'Please enter your postal code.',
                    'max_length': 'Postal code is too long.',
                },
                'country': {
                    'required': 'Please select your country.',
                },
                'county': {
                    'required': 'Please enter your county or region.',
                    'max_length': 'County/region name is too long.',
                },
        }

    def __init__(self, *args, **kwargs):
        """
        Method to add placeholders, classes and customize
        how the fields look like (auto-focus)
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2 (Optional)',
            'city': 'City',
            'postcode': 'Postal Code',
            'country': 'Country',
            'county': 'County / Region',
        }

        # Define autocomplete hints for each form field
        autocomplete_attrs = {
            'first_name': 'given-name',
            'last_name': 'family-name',
            'email': 'email',
            'phone_number': 'tel',
            'street_address_1': 'address-line1',
            'street_address_2': 'address-line2',
            'city': 'address-level2',
            'county': 'address-level1',
            'postcode': 'postal-code',
            'country': 'country-name',
        }


        # Make First name field autofocus
        self.fields['first_name'].widget.attrs['autofocus'] = True
        # Check if the field is required
        for field_name, field in self.fields.items():
            if field.required:
                placeholder = f'{placeholders[field_name]} *' # Add with star if it's required
            else:
                placeholder = placeholders[field_name]

            field.widget.attrs['placeholder'] = placeholder # Otherwise placeholder only
            field.widget.attrs['class'] = 'stripe-style'

            # Auto-complete
            if field_name in autocomplete_attrs:
                field.widget.attrs['autocomplete'] = autocomplete_attrs[field_name]

            # Remove the default labels from django forms
            field.label = False