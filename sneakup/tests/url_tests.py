import pytest

@pytest.mark.django_db
def test_home_url_includes(client):
    response = client.get('/')
    assert response.status_code in [200, 301, 302]

@pytest.mark.django_db
def test_products_url_includes(client):
    response = client.get('/products/')
    assert response.status_code in [200, 301, 302]

@pytest.mark.django_db
def test_checkout_url_includes(client):
    response = client.get('/checkout/')
    assert response.status_code in [200, 301, 302]

