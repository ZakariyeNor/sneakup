import pytest
from django.test import Client

client = Client()

@pytest.mark.django_db
def test_custom_404_view_renders_template():
    response = client.get('/non-existent-url/')
    assert response.status_code == 404
    assert 'errors/404.html' in [t.name for t in response.templates]
