from django.shortcuts import render, get_object_or_404
from .models import Profile

# Profile view
def profile(request):
    """
    User profile view
    """
    profile = get_object_or_404(Profile, user=request.user)
    return render(
        request,
        template_name= 'profiles/profile.html',
        context = {
            'profile': profile,
        }
    )