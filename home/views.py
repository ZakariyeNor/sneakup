from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from products.models import Product, Category
from .models import NewsletterSubscriber
from django.contrib import messages

from django.templatetags.static import static


# Home view
def index(request):
    """ A view to render home page"""

    products = Product.objects.all()
    category = Category.objects.all()

    if products.exists():
        messages.info(request, f"Welcome to DUAC! We have {category.count()} categories available.")
    else:
        messages.warning(request, "Currently, there are no categories available. Please check back later.")

    return render(request, "home/index.html", {
        "company_name": "Lanezra",
        "products": products,
    })


# Email subscription view
def email_subscribe(request):
    """
    Handles newsletter email subscriptions.
    """
    if request.method == 'POST':
        # Get the email
        email = request.POST.get('email')


        if email:
            try:
                # Validate email format
                validate_email(email)

                # Prevent duplication
                if not NewsletterSubscriber.objects.filter(email=email).exists():
                    NewsletterSubscriber.objects.create(email=email)
                    messages.success(request, 'Thanks for subscribing!')
                else:
                    messages.info(request, 'This email is already subscribed.')
            except ValidationError:
                messages.error(request, 'Please enter a valid email address.')
        else:
            messages.error(request, 'Email field cannot be empty.')
            return redirect('home')

    # Redirect back to home page
    # if someone accesses it via GET
    return redirect('home')
