from django.shortcuts import render, redirect, reverse
from .models import PrivacyPolicy, ReturnsPolicy
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