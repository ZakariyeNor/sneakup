import pytest
from django.urls import reverse
from django.contrib.messages import get_messages
from products.models import Product
from django.test import RequestFactory

@pytest.mark.django_db
class TestBagViews:

    def test_add_to_bag_post_free_size_new_product(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('add_to_bag', args=[product.id])

        response = client.post(url, data={
            'quantity': '2',
            'redirect_url': '/'
        }, follow=True)

        session = client.session
        assert str(product.id) in session['bag']
        assert session['bag'][str(product.id)] == 2

        messages = list(get_messages(response.wsgi_request))
        assert any("Added 2 x" in m.message for m in messages)
        assert response.redirect_chain[-1][0] == '/'

    def test_add_to_bag_post_free_size_existing_product(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('add_to_bag', args=[product.id])

        session = client.session
        session['bag'] = {str(product.id): 1}
        session.save()

        response = client.post(url, data={
            'quantity': '3',
            'redirect_url': '/'
        }, follow=True)

        session = client.session
        assert session['bag'][str(product.id)] == 4  # 1 + 3
        messages = list(get_messages(response.wsgi_request))
        assert any("Added 3 x" in m.message for m in messages)

    def test_add_to_bag_post_sized_product_with_size(self, client, db):
        product = Product.objects.create(name="SizedProduct", price=20, free_size=False)
        url = reverse('add_to_bag', args=[product.id])

        response = client.post(url, data={
            'quantity': '2',
            'selected_size': 'M',
            'redirect_url': '/'
        }, follow=True)

        session = client.session
        bag = session['bag']
        assert str(product.id) in bag
        assert bag[str(product.id)]['M'] == 2

        messages = list(get_messages(response.wsgi_request))
        assert any("Added 2 x" in m.message for m in messages)

    def test_add_to_bag_post_sized_product_without_size_shows_error(self, client, db):
        product = Product.objects.create(name="SizedProduct", price=20, free_size=False)
        url = reverse('add_to_bag', args=[product.id])

        referer = '/'
        response = client.post(
            url,
            data={'quantity': '1', 'redirect_url': '/'},
            HTTP_REFERER=referer,
            follow=True,
        )

        messages = list(get_messages(response.wsgi_request))
        assert any("Please select a size before adding" in m.message for m in messages)
        # Redirect back to referer
        assert response.redirect_chain[-1][0] == referer

    def test_add_to_bag_invalid_quantity_redirects_with_error(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('add_to_bag', args=[product.id])

        response = client.post(url, data={
            'quantity': 'abc',
            'redirect_url': '/'
        }, follow=True)

        messages = list(get_messages(response.wsgi_request))
        assert any("Invalid quantity provided" in m.message for m in messages)

    def test_add_to_bag_invalid_quantity_out_of_range_redirects_with_error(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('add_to_bag', args=[product.id])

        response = client.post(url, data={
            'quantity': '20',
            'redirect_url': '/'
        }, follow=True)

        messages = list(get_messages(response.wsgi_request))
        assert any("Invalid quantity. Please select between 1 and 10." in m.message for m in messages)

    def test_add_to_bag_get_redirects_to_products(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('add_to_bag', args=[product.id])

        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse('products')

    def test_update_bag_free_size_update_quantity(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('update_bag', args=[product.id])

        session = client.session
        session['bag'] = {str(product.id): 2}
        session.save()

        response = client.post(url, data={
            'quantity': '5',
            'redirect_url': '/bag/'
        }, follow=True)

        session = client.session
        assert session['bag'][str(product.id)] == 5
        messages = list(get_messages(response.wsgi_request))
        assert any("Updated" in m.message for m in messages)
        assert response.redirect_chain[-1][0] == '/bag/'

    def test_update_bag_free_size_remove_item(self, client, db):
        product = Product.objects.create(name="FreeSizeProduct", price=10, free_size=True)
        url = reverse('update_bag', args=[product.id])

        session = client.session
        session['bag'] = {str(product.id): 2}
        session.save()

        response = client.post(url, data={
            'quantity': '0',
            'redirect_url': '/bag/'
        }, follow=True)

        session = client.session
        assert str(product.id) not in session['bag']
        messages = list(get_messages(response.wsgi_request))
        assert any("Removed" in m.message for m in messages)

    def test_update_bag_sized_product_update_quantity(self, client, db):
        product = Product.objects.create(name="SizedProduct", price=10, free_size=False)
        url = reverse('update_bag', args=[product.id])

        session = client.session
        session['bag'] = {str(product.id): {'M': 2}}
        session.save()

        response = client.post(url, data={
            'quantity': '3',
            'selected_size': 'M',
            'redirect_url': '/bag/'
        }, follow=True)

        session = client.session
        assert session['bag'][str(product.id)]['M'] == 3
        messages = list(get_messages(response.wsgi_request))
        assert any("Updated" in m.message for m in messages)

    def test_update_bag_sized_product_remove_size(self, client, db):
        product = Product.objects.create(name="SizedProduct", price=10, free_size=False)
        url = reverse('update_bag', args=[product.id])

        session = client.session
        session['bag'] = {str(product.id): {'M': 1}}
        session.save()

        response = client.post(url, data={
            'quantity': '0',
            'selected_size': 'M',
            'redirect_url': '/bag/'
        }, follow=True)

        session = client.session
        assert str(product.id) not in session['bag']
        messages = list(get_messages(response.wsgi_request))
        assert any("Removed" in m.message for m in messages)

    def test_update_bag_get_redirects_to_bag(self, client):
        url = reverse('update_bag', args=[1])
        response = client.get(url)
        assert response.status_code == 302
        assert response.url == reverse('bag')
