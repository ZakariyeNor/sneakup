import pytest
from django import forms
from products.forms import ProductForm
from products.models import Category, Product


@pytest.mark.django_db
def test_product_form_requires_category():
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'Test description',
        'size': ['38'],
        'free_size': False,
        # No category provided
    })
    assert not form.is_valid()
    assert 'Please select a category.' in form.errors['__all__'][0]


@pytest.mark.django_db
def test_product_form_free_size_and_sizes_mutually_exclusive():
    category = Category.objects.create(name='cat1', friendly_name='Cat 1')
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'desc',
        'category': category.id,
        'size': ['38', '39'],
        'free_size': True,
    })
    assert not form.is_valid()
    assert "Choose either specific sizes or Free Size" in form.errors[
            '__all__'][0]


@pytest.mark.django_db
def test_product_form_requires_size_or_free_size():
    category = Category.objects.create(name='cat1', friendly_name='Cat 1')
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'desc',
        'category': category.id,
        'size': [],
        'free_size': False,
    })
    assert not form.is_valid()
    assert "You must either select at least"
    "one size or check Free Size." in form.errors['__all__'][0]


@pytest.mark.django_db
def test_product_form_clean_sizes_string_to_list():
    category = Category.objects.create(name='cat1', friendly_name='Cat 1')
    # Pass size as list with one string item (simulate realistic form POST)
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'desc',
        'category': category.id,
        'size': ['38'],  # a list with one size string
        'free_size': False,
    })
    assert form.is_valid()
    cleaned_data = form.clean()
    assert cleaned_data['size'] == ['38']


@pytest.mark.django_db
def test_product_form_valid_with_sizes():
    category = Category.objects.create(name='cat1', friendly_name='Cat 1')
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'desc',
        'category': category.id,
        'size': ['38', '39'],
        'free_size': False,
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_product_form_valid_with_free_size():
    category = Category.objects.create(name='cat1', friendly_name='Cat 1')
    form = ProductForm(data={
        'name': 'Test Product',
        'price': '10.00',
        'description': 'desc',
        'category': category.id,
        'size': [],
        'free_size': True,
    })
    assert form.is_valid()


@pytest.mark.django_db
def test_form_init_sets_category_queryset_and_labels():
    category1 = Category.objects.create(name='cat1', friendly_name='Cat One')
    category2 = Category.objects.create(name='cat2', friendly_name='Cat Two')
    form = ProductForm()

    # Categories ordered by friendly_name
    categories = list(form.fields['category'].queryset)
    assert categories == sorted(categories, key=lambda c: c.friendly_name)

    # Label from instance uses friendly_name or name
    label1 = form.fields['category'].label_from_instance(category1)
    label2 = form.fields['category'].label_from_instance(category2)
    assert label1 == category1.friendly_name
    assert label2 == category2.friendly_name

    # Empty label is set
    assert form.fields['category'].empty_label == 'Select Category'

    # Description widget attrs
    assert form.fields['description'].widget.attrs.get('rows') == 4
    assert 'form-control' in form.fields[
        'description'
        ].widget.attrs.get('class', '')

    # free_size label is marked safe and contains padding style
    assert 'padding-left' in form.fields['free_size'].label

    # name field has autofocus attribute
    assert form.fields['name'].widget.attrs.get('autofocus') is True
