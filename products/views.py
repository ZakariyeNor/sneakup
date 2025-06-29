from django.shortcuts import render
from .models import Product
from django.conf import settings


# Products view
def all_products_view(request):
    """
    View to show all products and filtering layout.
    """
    products = Product.objects.all()
    template = 'products/products.html'
    marketing_Shoe = settings.MEDIA_URL + 'marketing_Shoe.jpg'
    context = {
        'products': products,
        "marketing_Shoe": marketing_Shoe,
    }

    return render(request, template, context)