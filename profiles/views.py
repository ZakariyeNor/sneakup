from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from checkout.models import Order, OrderLineItem
from checkout.forms import OrderForm

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

# Individual order detail view
def order_detail(request, order_number):
    """
    A view to show a specific order details
    """
    order = get_object_or_404(Order, order_number=order_number)
    order_form = OrderForm(instance=order)
    lineitems = order.lineitems.all()
    messages.info(
        request,
        (
            f'This is a confirmation summary for order { order_number }.'
        )
    )

    return render(
        request,
        template_name= 'checkout/checkout.html',
        context = {
            'order': order,
            'lineitems': lineitems,
            'order_form': order_form,
            'from_profile': True,
        }
    )