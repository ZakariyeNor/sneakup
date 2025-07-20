import pytest
from profiles.forms import ProfileForm

@pytest.mark.django_db
def test_profile_form_placeholders_and_labels():
    form = ProfileForm()

    placeholders = {
        'default_phone_number': 'Phone Number',  # no star here
        'default_street_address_1': 'Street Address 1',
        'default_street_address_2': 'Street Address 2 (Optional)',
        'default_city': 'City',
        'default_postcode': 'Postal Code',
        'default_county': 'County / Region',
        'default_country': '',
    }

    for field_name, expected_placeholder in placeholders.items():
        assert form.fields[field_name].label is False
        if field_name == 'default_country':
            assert form.fields[field_name].widget.attrs.get('placeholder') in (None, '')
        else:
            assert form.fields[field_name].widget.attrs['placeholder'] == expected_placeholder

    assert form.fields['default_phone_number'].widget.attrs.get('autofocus') is True


@pytest.mark.django_db
def test_profile_form_valid_empty_data():
    # Because fields are optional (blank=True), empty data is valid
    data = {}
    form = ProfileForm(data=data)
    assert form.is_valid()
