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

    """
    Category querying by name or description
    """

    if request.GET:
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
    }

    return render(request, template, context)
    