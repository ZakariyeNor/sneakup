from django.shortcuts import render, redirect, reverse
from .models import PrivacyPolicy
from django.contrib import messages

# Privacy-policy view
def privacy_policy(request):
    # Get the last uploaded document
    privacy_policy = PrivacyPolicy.objects.order_by('-updated_at').first()
    
    template = 'pages/privacy_policy.html',
    context = {
        'privacy_policy': privacy_policy,
    }

    return render(request, template, context)
