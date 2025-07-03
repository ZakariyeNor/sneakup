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
    # check what's posted
    print("POST data:", request.POST)
    if request.method == "POST":
        item_id = str(item_id)
        quantity = int(request.POST.get('quantity'))
        # Get the current url to redirect the user when the product is added into the bag
        redirect_url = request.POST.get('redirect_url')
        # Get size from the request
        size = request.POST.get('selected_size')
        # check if the size sends withe form
        print("Selected size from POST:", size)

        # Get the bag from the session or create one
        bag = request.session.get('bag', {})
        # Get product from the session
        product = get_object_or_404(Product, pk=item_id)

        # Check if the product is free size
        if product.free_size:
            # Check if it's in the bag and increment if it's in the bag
            if item_id in bag:
                bag[item_id] += quantity
            # Otherwise add the product as a free size one
            else:
                bag[item_id] = quantity
        # If product has size
        else:
            # Check if the product is in the bag
            if item_id in bag:
                # Increment the quantity with it's size only
                # if the size is already exists in the bag
                if isinstance(bag[item_id], dict):
                    if size in bag[item_id]:
                        bag[item_id][size] += quantity
                    # Other wise add the product to the bag with it's size
                    else:
                        bag[item_id][size] = quantity
                # If the product is old format change it to store size with it's quantity
                else:
                    bag[item_id] = {size: quantity}
            # If the item is not in the bag
            else:
                bag[item_id] = {size: quantity}
        print("Bag before saving:", bag)
        # Save the product
        request.session['bag'] = bag
        return redirect(redirect_url)

    # Redirect the user back to shp page if the method is not POST
    return redirect('products') 

    