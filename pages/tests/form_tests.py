# pages/tests/form_tests.py

import pytest
from pages.forms import ContactMessageForm

@pytest.mark.django_db
def test_contact_form_valid_data():
    form_data = {
        'full_name': 'Jane Doe',
        'email': 'jane@example.com',
        'order_number': '123ABC',
        'message': 'This is a test message.',
        'send_info': True,
    }
    form = ContactMessageForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_contact_form_missing_required_fields():
    form = ContactMessageForm(data={})
    assert not form.is_valid()
    assert 'full_name' in form.errors
    assert 'email' in form.errors
    assert 'message' in form.errors

def test_contact_form_field_placeholders_and_labels():
    form = ContactMessageForm()
    assert form.fields['full_name'].widget.attrs['placeholder'] == 'Full Name'
    assert form.fields['email'].widget.attrs['placeholder'] == 'Email Address'
    assert form.fields['order_number'].widget.attrs['placeholder'] == 'Order Number (optional)'
    assert form.fields['message'].widget.attrs['placeholder'] == 'Type your message here...'
    assert form.fields['message'].widget.attrs['rows'] == 5
    for field in form.fields:
        assert form.fields[field].label is False

def test_contact_form_autofocus_is_set():
    form = ContactMessageForm()
    assert form.fields['full_name'].widget.attrs.get('autofocus') is True
