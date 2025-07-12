from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Profile view
def profile(request):
    """
    User profile view
    """
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    return render(
        request,
        template_name= 'profiles/profile.html',
        context = {
            'orders': orders,
            'profile_form': profile_form,
        }
    )