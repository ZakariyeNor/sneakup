from django.shortcuts import render, redirect, reverse
from .models import PrivacyPolicy, ReturnsPolicy, FAQs, ContactMessage
from .forms import ContactMessageForm
from django.contrib import messages

# Privacy-policy view
def privacy_policy(request):
    # Get the last uploaded document
    privacy_policy = PrivacyPolicy.objects.order_by('-updated_at').first()
    
    template = 'pages/privacy_policy.html'
    context = {
        'privacy_policy': privacy_policy,
    }

    return render(request, template, context)


# Returns-policy view
def returns_policy(request):
    # Get the last uploaded document
    returns_policy = ReturnsPolicy.objects.order_by('-updated_at').first()
    
    template = 'pages/returns_policy.html'
    context = {
        'returns_policy': returns_policy,
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
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
    else:
        contact_form = ContactMessageForm()
    
    template = 'pages/contact_message.html'
    context = {
        'contact_form': contact_form,
        'on_contact': True,
    }
    return render(request, template, context)