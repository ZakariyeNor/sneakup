import pytest
from django.urls import resolve, reverse
from bag import views  # Adjust if your app is named differently

@pytest.mark.django_db
def test_bag_url_resolves_to_view_bag():
    path = reverse('bag')
    resolved = resolve(path)
    assert resolved.func == views.view_bag

@pytest.mark.django_db
def test_add_to_bag_url_resolves():
    path = reverse('add_to_bag', args=[123])
    resolved = resolve(path)
    assert resolved.func == views.add_to_bag

@pytest.mark.django_db
def test_update_bag_url_resolves():
    # item_id is a string path param in update url
    path = reverse('update_bag', args=['abc123'])
    resolved = resolve(path)
    assert resolved.func == views.update_bag
