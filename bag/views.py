from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Bag view
def view_bag(request):
    """
    A view to show the bag
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add the chosen quantity of the product in the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)