import json
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def event():
    intent_mock = MagicMock()
    intent_mock.id = 'pi_123456789'
    intent_mock.metadata.bag = json.dumps({'1': 2})
    intent_mock.metadata.save_info = True
    intent_mock.metadata.name = 'testuser'
    intent_mock.latest_charge = 'ch_123456789'

    shipping_mock = MagicMock()
    shipping_mock.phone = '1234567890'
    shipping_mock.name = 'John Doe'
    shipping_mock.address.line1 = '123 Main St'
    shipping_mock.address.line2 = ''
    shipping_mock.address.city = 'Townsville'
    shipping_mock.address.state = 'State'
    shipping_mock.address.postal_code = '12345'
    shipping_mock.address.country = 'SE'

    intent_mock.shipping = shipping_mock

    event_mock = MagicMock()
    event_mock.type = 'payment_intent.succeeded'
    event_mock.data.object = intent_mock

    return event_mock
