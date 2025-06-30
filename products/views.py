from django.shortcuts import render,redirect, reverse
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

    if request.GET:
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
    }

    return render(request, template, context)
    