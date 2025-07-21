import pytest
from products.models import Category, Product


@pytest.mark.django_db
def test_category_str_and_friendly_name():
    category = Category.objects.create(
            name="Sneakers", friendly_name="Cool Sneakers")
    assert str(category) == "Sneakers"
    assert category.display_friendly_name() == "Cool Sneakers"


@pytest.mark.django_db
def test_product_str_and_size_list_with_sizes():
    category = Category.objects.create(name="Sneakers")
    product = Product.objects.create(
        name="Air Max",
        subtitle="Running shoe",
        sku="AM123",
        description="Comfortable running shoe",
        category=category,
        size='["7", "8", "9"]',  # JSONField as a JSON string
        free_size=False,
        price=120.00,
        rating=4.5,
        image_url="http://example.com/image.jpg",
        image=None
    )
    assert str(product) == "Air Max"
    assert product.size_list() == ['["7"', ' "8"', ' "9"]']


@pytest.mark.django_db
def test_product_size_list_empty_and_free_size():
    product = Product.objects.create(
        name="One Size Hat",
        description="Universal fit",
        price=25.00,
        free_size=True
    )
    assert product.size_list() == []
    assert product.free_size is True


@pytest.mark.django_db
def test_product_size_list_with_none_size():
    product = Product.objects.create(
        name="No Size Product",
        description="No sizes available",
        price=10.00,
        free_size=False,
        size=None
    )
    assert product.size_list() == []
