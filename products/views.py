from django.shortcuts import render,redirect, reverse,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm

import ast

# Products view
def all_products_view(request):
    """
    View to show all products and filtering layout.
    """
    products = Product.objects.all()

    search = None
    categories = None
    sort = None

    if request.GET:
        # Sort products by price and rating
        if 'sort' in request.GET:
            sort = request.GET['sort']

            # sorting direction of the price and rating based on the request
            if sort == 'price_asc':
                products = products.order_by('price')
                messages.info(request, "Sorted products by price: low to high.")
            elif sort == 'price_desc':
                products = products.order_by('-price')
                messages.info(request, "Sorted products by price: high to low.")

            elif sort == 'rating_asc':
                products = products.order_by('rating')
                messages.info(request, "Sorted products by rating: low to high.")
            elif sort == 'rating_desc':
                products = products.order_by('-rating')
                messages.info(request, "Sorted products by rating: high to low.")

        current_sorting = sort

        # Querying products based on their categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            messages.info(request, f"Filtered products by categories: {', '.join([c.name for c in categories])}")

        # Searching products in the search input field by name or description
        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(request, "Search field is empty. Try entering something.")
                return redirect(reverse('products'))
            
            searches = Q(name__icontains=search) | Q(description__icontains=search)
            products = products.filter(searches)
            if products.exists():
                messages.success(request, f"Found {products.count()} products matching '{search}'.")
            else:
                messages.warning(request, f"No products found matching '{search}'.")

    template = 'products/products.html'
    context = {
        'products': products,
        'search_term': search,
        'current_categories': categories,
        'current_sorting': sort,
    }

    return render(request, template, context)


# Product detail view
def product_detail(request, product_id):
    """ A view to show an individual product """
    product = get_object_or_404(Product, pk=product_id)
    if not product.size:
        product.size = []

    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)


# Add products view loged in required decorator
@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only store administrators are authorized to do this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            product = product_form.save()
            messages.success(
                request,
                'You successfully added a new product to the product listings.'
            )
            return redirect('product_detail', product_id=product.id)
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        product_form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }
    return render(request, template, context)


# Edit product view loged in required decorator
@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only store administrators are authorized to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product = product_form.save()
            messages.success(
                request,
                f'You successfully updated the {product.name}.'
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Update failed. Please ensure all required fields are correctly filled.'
            )
    else:
        product_form = ProductForm(instance=product)
        messages.info(
            request, 
            f'Youre editing {product.name}' 
        )
    template = 'products/edit_product.html'
    context = {
        'product_form': product_form,
        'product': product,
    }
    return render(request, template, context)


# Delete product view loged in required decorator
@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only store administrators are authorized to do this.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has been deleted.')
    return redirect('products')