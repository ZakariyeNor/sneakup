import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_all_products_view(client, django_user_model):
    url = reverse('products')

    # Create categories and products
    cat1 = Category.objects.create(name='Shoes')
    cat2 = Category.objects.create(name='Clothing')
    p1 = Product.objects.create(
        name='Nike Air', price=50, category=cat1,
        description='Great shoes', sku='SKU1')
    p2 = Product.objects.create(
        name='Adidas Shirt', price=30, category=cat2,
        description='Comfortable', sku='SKU2')

    # Basic GET without filters
    response = client.get(url)
    assert response.status_code == 200
    assert 'products/products.html' in [t.name for t in response.templates]
    assert list(response.context['products']) == [p1, p2]

    # Test sorting by price ascending
    response = client.get(url + '?sort=price_asc')
    assert response.status_code == 200
    products = list(response.context['products'])
    assert products[0].price <= products[1].price
    assert b'Sorted products by price: low to high.' in response.content

    # Test sorting by rating descending (products have null rating by default)
    response = client.get(url + '?sort=rating_desc')
    assert response.status_code == 200

    # Test filtering by category
    response = client.get(url + '?category=Shoes')
    assert response.status_code == 200
    for product in response.context['products']:
        assert product.category.name == 'Shoes'

    # Test searching with results
    response = client.get(url + '?q=Nike')
    assert response.status_code == 200
    assert b'Found 1 products matching' in response.content

    # Test searching with no results
    response = client.get(url + '?q=NoMatchProduct')
    assert response.status_code == 200
    assert b'No products found matching' in response.content

    # Test searching with empty query redirects with error message
    response = client.get(url + '?q=')
    assert response.status_code == 302  # Redirect


@pytest.mark.django_db
def test_product_detail_view(client):
    category = Category.objects.create(name='Shoes')
    product = Product.objects.create(
        name='Test Product', price=100, category=category,
        description='desc', sku='SKU123')

    url = reverse('product_detail', args=[product.id])
    response = client.get(url)
    assert response.status_code == 200
    assert 'products/product_detail.html' in [
            t.name for t in response.templates]
    assert response.context['product'] == product


@pytest.mark.django_db
def test_add_product_view_permissions_and_post(client, django_user_model):
    url = reverse('add_product')

    # Non-logged in user redirects to login
    response = client.get(url)
    assert response.status_code == 302

    # Logged in but not superuser: redirected with error
    user = django_user_model.objects.create_user(
        username='user', password='pass')
    client.login(username='user', password='pass')
    response = client.get(url)
    assert response.status_code == 302

    # Superuser access GET
    admin_user = django_user_model.objects.create_superuser(
        username='admin', password='pass')
    client.login(username='admin', password='pass')
    response = client.get(url)
    assert response.status_code == 200
    assert 'products/add_product.html' in [t.name for t in response.templates]

    # Superuser POST valid data
    category = Category.objects.create(name='Shoes')
    post_data = {
        'name': 'New Shoe',
        'price': 99.99,
        'category': category.id,
        'description': 'Nice shoe',
        'sku': 'SKU999',
        'free_size': True,
    }
    response = client.post(url, post_data)
    assert response.status_code == 302  # Redirect after success
    assert Product.objects.filter(name='New Shoe').exists()


@pytest.mark.django_db
def test_edit_product_view_permissions_and_post(client, django_user_model):
    category = Category.objects.create(name='Shoes')
    product = Product.objects.create(
        name='EditMe', price=10, category=category,
        description='desc', sku='SKU555')

    url = reverse('edit_product', args=[product.id])

    # Non-logged in user redirect
    response = client.get(url)
    assert response.status_code == 302

    # Logged in non-superuser redirect with error
    user = django_user_model.objects.create_user(
        username='user', password='pass')
    client.login(username='user', password='pass')
    response = client.get(url)
    assert response.status_code == 302

    # Superuser GET
    admin_user = django_user_model.objects.create_superuser(
        username='admin', password='pass')
    client.login(username='admin', password='pass')
    response = client.get(url)
    assert response.status_code == 200
    assert 'products/edit_product.html' in [t.name for t in response.templates]

    # Superuser POST valid update
    post_data = {
        'name': 'Edited Name',
        'price': 20,
        'category': category.id,
        'description': 'Updated desc',
        'sku': 'SKU555',
        'free_size': True,
    }
    response = client.post(url, post_data)
    assert response.status_code == 302
    product.refresh_from_db()
    assert product.name == 'Edited Name'


@pytest.mark.django_db
def test_delete_product_view_permissions(client, django_user_model):
    category = Category.objects.create(name='Shoes')
    product = Product.objects.create(
        name='DeleteMe', price=10, category=category,
        description='desc', sku='SKU777')

    url = reverse('delete_product', args=[product.id])

    # Non-logged in user redirected
    response = client.post(url)
    assert response.status_code == 302

    # Logged in non-superuser redirected with error
    user = django_user_model.objects.create_user(
        username='user', password='pass')
    client.login(username='user', password='pass')
    response = client.post(url)
    assert response.status_code == 302
    assert Product.objects.filter(id=product.id).exists()

    # Superuser can delete
    admin_user = django_user_model.objects.create_superuser(
        username='admin', password='pass')
    client.login(username='admin', password='pass')
    response = client.post(url)
    assert response.status_code == 302
    assert not Product.objects.filter(id=product.id).exists()
