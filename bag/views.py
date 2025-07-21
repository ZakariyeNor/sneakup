from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib import messages


# Bag view
def view_bag(request):
    """
    A view to show the bag
    """
    return render(request, 'bag/bag.html')


# Add to bag view
def add_to_bag(request, item_id):
    """ Add the chosen quantity of the product in the shopping bag """

    # check what's posted
    print("POST data:", request.POST)
    if request.method != "POST":
        # Redirect the user back to shp page if the method is not POST
        return redirect('products')
    # Convert item_id to string
    item_id = str(item_id)

    # Get redirect url from the POST data
    redirect_url = request.POST.get('redirect_url', 'products')

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        messages.error(request, 'Invalid quantity provided.')
        return redirect(request.META.get('HTTP_REFERER', 'products'))

    # Defensive validation
    if quantity < 1 or quantity > 10:
        messages.error(
            request,
            'Invalid quantity. Please select between 1 and 10.'
        )
        return redirect(request.POST.get('redirect_url'))

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
        messages.success(
                request, f"Added {quantity} x '{product.name}' to your bag.")
    # If product has size
    else:
        if not size:
            messages.error(
                request,
                "Please select a size before adding the product to your bag.")
            return redirect(request.META.get('HTTP_REFERER', 'products'))
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
                # If the product is old format change it
                # to store size with it's quantity
                else:
                    bag[item_id] = {size: quantity}
            # If the item is not in the bag
            else:
                bag[item_id] = {size: quantity}
            messages.success(
                request,
                f"Added {quantity} x '{product.name}'"
                "(size {size}) to your bag.")

    print("Bag before saving:", bag)
    # Save the product
    request.session['bag'] = bag
    return redirect(redirect_url)


# Update the bag items view
def update_bag(request, item_id):
    """
    A view to update the specific item in the
    shopping bag
    """
    if request.method == "POST":
        # Get the quantity from POST data or assume the quantity is 0
        quantity = int(request.POST.get('quantity', 1))

        # Get the selected size from POST data if provided
        size = request.POST.get('selected_size')

        # Get redirect URL from POST data or 'bag' page if missing
        redirect_url = request.POST.get('redirect_url', 'bag')

        # Retrieve the current shopping bag from session (or create empty dict)
        bag = request.session.get('bag', {})

        # Fetch the product object by its ID.
        product = get_object_or_404(Product, pk=item_id)

        # Handle product that is free size
        if product.free_size:
            if quantity > 0:
                # Update or add product quantity in the bag directly by item ID
                bag[item_id] = quantity
                messages.success(
                    request,
                    f"Updated '{product.name}' quantity to {quantity}.")
            else:
                # Remove product from the bag if quantity is 0 or less
                bag.pop(item_id, None)
                messages.info(
                        request, f"Removed '{product.name}' from your bag.")
        else:
            # Handle product that has size variations
            if quantity > 0:
                if item_id in bag:
                    # Update quantity for the specific size of the product
                    bag[item_id][size] = quantity
                else:
                    # Add product with size and
                    # quantity as a new entry in the bag
                    bag[item_id] = {size: quantity}
                messages.success(
                    request,
                    f"Updated '{product.name}'"
                    "(size {size}) quantity to {quantity}."
                    )
            else:
                # Remove the size variant of the
                # product if quantity is 0 or less
                if item_id in bag and size in bag[item_id]:
                    del bag[item_id][size]
                    messages.info(
                        request,
                        f"Removed size {size} of"
                        "'{product.name}' from your bag.")
                    # If no sizes remain for this product,
                    # remove the product entry entirely
                    if not bag[item_id]:
                        bag.pop(item_id)
                        messages.info(
                            request,
                            f"Removed '{product.name}'"
                            "entirely from your bag.")

        # Save the updated bag
        request.session['bag'] = bag

        # Redirect the user back to the given URL (shopping bag page)
        return redirect(redirect_url)

    return redirect('bag')
