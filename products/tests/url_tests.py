import pytest
from django.urls import reverse, resolve
from products import views
from django.contrib.auth.models import User

PRODUCTS_PREFIX = '/products'

@pytest.mark.django_db
def test_products_url_resolves():
    assert resolve(f'{PRODUCTS_PREFIX}/').func == views.all_products_view

@pytest.mark.django_db
def test_product_detail_url_resolves():
    assert resolve(f'{PRODUCTS_PREFIX}/product_detail/1/').func == views.product_detail

@pytest.mark.django_db
def test_add_product_url_resolves():
    assert resolve(f'{PRODUCTS_PREFIX}/add_product/').func == views.add_product

@pytest.mark.django_db
def test_edit_product_url_resolves():
    assert resolve(f'{PRODUCTS_PREFIX}/edit_product/1/').func == views.edit_product

@pytest.mark.django_db
def test_delete_product_url_resolves():
    assert resolve(f'{PRODUCTS_PREFIX}/delete_product/1/').func == views.delete_product


@pytest.mark.django_db
def test_access_urls(client, django_user_model):
    # Create superuser
    admin_user = django_user_model.objects.create_superuser(username='admin', password='pass')
    client.login(username='admin', password='pass')

    # Test all_products_view accessible by anyone (no login required)
    response = client.get(reverse('products'))
    assert response.status_code == 200

    # Test product_detail view accessible by anyone (simulate product exists)
    from products.models import Category, Product
    category = Category.objects.create(name='TestCat')
    product = Product.objects.create(name='TestProd', price=10, category=category, description='desc')
    response = client.get(reverse('product_detail', args=[product.id]))
    assert response.status_code == 200

    # Add product, edit product, delete product require superuser
    response = client.get(reverse('add_product'))
    assert response.status_code == 200

    response = client.get(reverse('edit_product', args=[product.id]))
    assert response.status_code == 200

    response = client.post(reverse('delete_product', args=[product.id]))
    # Should redirect after delete
    assert response.status_code in (302, 303)


@pytest.mark.django_db
def test_non_superuser_cannot_access_admin_views(client, django_user_model):
    user = django_user_model.objects.create_user(username='user', password='pass')
    client.login(username='user', password='pass')

    from products.models import Category, Product
    category = Category.objects.create(name='TestCat')
    product = Product.objects.create(name='TestProd', price=10, category=category, description='desc')

    # Add product redirects
    response = client.get(reverse('add_product'))
    assert response.status_code == 302

    # Edit product redirects
    response = client.get(reverse('edit_product', args=[product.id]))
    assert response.status_code == 302

    # Delete product redirects
    response = client.post(reverse('delete_product', args=[product.id]))
    assert response.status_code == 302
