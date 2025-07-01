from django.shortcuts import render,redirect, reverse,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from django.conf import settings


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
            elif sort == 'price_desc':
                products = products.order_by('-price')

            elif sort == 'rating_asc':
                products = products.order_by('rating')
            elif sort == 'rating_desc':
                products = products.order_by('-rating')
        current_sorting = sort

        # Qeueriying products based on their categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Searching products in the search input field by name or description
        if 'q' in request.GET:
            search = request.GET['q']
            if not search:
                messages.error(request, "Search field is empty. Try entering something.")
                return redirect(reverse('products'))
            
            searches = Q(name__icontains=search) | Q(description__icontains=search)
            products = products.filter(searches)


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
    template = 'products/product_detail.html'
    context = {
        'product': product,
    }

    return render(request, template, context)