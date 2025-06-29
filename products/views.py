from django.shortcuts import render
from .models import Product


# Products view
def all_products_view(request):
    """
    View to show all products and filtering layout.
    """
    products = Product.objects.all()
    template = 'products/products.html'
    context = {
        'products': products,
    }

    return render(request, template, context)