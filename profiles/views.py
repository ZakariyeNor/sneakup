from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm

# Profile view
def profile(request):
    """
    User profile view
    """
    profile = get_object_or_404(Profile, user=request.user)

    # Update logic
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        # Check the form and save it if it's truthy
        if profile_form.is_valid():
            profile_form.save()
            messages.success(
                request,
                'Your profile has been updated successfully.'
            )


    profile_form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    return render(
        request,
        template_name= 'profiles/profile.html',
        context = {
            'orders': orders,
            'profile_form': profile_form,
            'on_profile': True,
        }
    )