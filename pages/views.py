from django.shortcuts import render, redirect, reverse
from .models import (
    PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage,
    AboutPageHero, OurMission, NewArrivals, OurMaterials,
    BestSelling, LaunchedProducts,
)
from .forms import ContactMessageForm
from django.contrib import messages

from cloudinary.utils import cloudinary_url


# Privacy-policy view
def privacy_policy(request):
    # Get the last uploaded document
    privacy_policy = PrivacyPolicy.objects.order_by('-updated_at').last()

    pdf_url = None
    if privacy_policy and privacy_policy.pdf:
        pdf_url, _ = cloudinary_url(
            privacy_policy.pdf.public_id + '.pdf',
            resource_type='raw',
            type='upload'
        )

    template = 'pages/privacy_policy.html'
    context = {
        'privacy_policy': privacy_policy,
        'pdf_url': pdf_url
    }

    return render(request, template, context)


# Returns-policy view
def returns_policy(request):
    # Get the last uploaded document
    returns_policy = ReturnsPolicy.objects.order_by('-updated_at').last()

    pdf_url = None
    if returns_policy and returns_policy.pdf:
        pdf_url, _ = cloudinary_url(
            returns_policy.pdf.public_id + '.pdf',
            resource_type='raw',
            type='upload'
        )

    template = 'pages/returns_policy.html'
    context = {
        'returns_policy': returns_policy,
        'pdf_url': pdf_url
    }

    return render(request, template, context)


# FAQs view
def faqs_view(request):
    # Display the faq and their answers on the view
    faqs = FAQs.objects.all()

    template = 'pages/faqs.html'
    context = {
        'faqs': faqs,
    }

    return render(request, template, context)


# Contact message view
def contact(request):
    # Display the faq and their answers on the view
    if request.method == 'POST':
        contact_form = ContactMessageForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        contact_form = ContactMessageForm()

    template = 'pages/contact_message.html'
    context = {
        'contact_form': contact_form,
        'on_contact': True,
    }
    return render(request, template, context)


def about_view(request):
    hero = AboutPageHero.objects.first()
    mission = OurMission.objects.first()
    materials = OurMaterials.objects.first()

    new_arrivals = NewArrivals.objects.all().order_by('-launched_date')[:4]
    best_selling = BestSelling.objects.first()
    launched_products = LaunchedProducts.objects.all().order_by(
            '-launched_date')[:4]

    context = {
        'hero': hero,
        'mission': mission,
        'materials': materials,
        'new_arrivals': new_arrivals,
        'best_selling': best_selling,
        'launched_products': launched_products,
    }
    return render(request, 'pages/about.html', context)
