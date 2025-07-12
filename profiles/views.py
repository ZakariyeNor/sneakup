from django.shortcuts import render
from .models import Profile

# Profile view
def profile(request):
    """
    User profile view
    """
    return render(
        request,
        template_name= 'profiles/profile.html',
        context = {}
    )