from django.shortcuts import render
from django.conf import settings
from products.models import Product, Category
from django.contrib import messages

# Create your views here.
def index(request):
    """ A view to render home page"""
    hero_image = settings.MEDIA_URL + 'hero_pict.jpg'
    sports = settings.MEDIA_URL + 'sports.jpg'
    running = settings.MEDIA_URL + 'running.jpg'
    casual = settings.MEDIA_URL + 'casual.jpg'
    formal = settings.MEDIA_URL + 'formal.jpg'
    summer_sale = settings.MEDIA_URL + 'summer_sale.jpg'
    products = Product.objects.all()
    category = Category.objects.all()
    
    
    if products.exists():
        messages.info(request, f"Welcome to DUAC! We have {category.count()} categories available.")
    else:
        messages.warning(request, "Currently, there are no categories available. Please check back later.")

    return render(request, "home/index.html", {
        "company_name": "Lanezra",
        "hero_image": hero_image,
        "running": running,
        "casual": casual,
        "formal": formal,
        "sports": sports,
        "summer_sale": summer_sale,
        "products": products,
    })