from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from shop.models import Product
from wishlist.models import Wishlist


# Create your views here.

def cart_summary(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart_summary.html')


def add_to_cart(request, item_id):
    """ Add a product to the shopping cart and remove it from the wishlist """

    product = get_object_or_404(Product, id=item_id)
    redirect_url = request.POST.get('redirect_url', 'wishlist')
    cart = request.session.get('cart', {})

    # Get quantity, default to 1 if not provided
    quantity = request.POST.get('quantity')
    try:
        quantity = int(quantity) if quantity else 1
    except ValueError:
        quantity = 1  # Fallback to 1 if invalid input

    # Add product to cart
    if str(item_id) in cart:
        cart[str(item_id)] += quantity
    else:
        cart[str(item_id)] = quantity

    # Remove product from wishlist (if it exists)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    if wishlist_item.exists():
        wishlist_item.delete()
        messages.success(request, f"{product.name} moved to cart and removed from wishlist!")
    else:
        messages.success(request, "Item added to your cart successfully!")

    # Save cart to session
    request.session['cart'] = cart

    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product in the cart."""
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    try:
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f"'{
                product.name}' has been updated to {quantity}.")
        else:
            cart.pop(item_id, None)
            messages.success(request, f"'{
                product.name}' has been removed from your cart.")
    except ValueError:
        messages.error(request, "Invalid quantity provided.")

    request.session['cart'] = cart
    return redirect(reverse('cart_summary'))


def remove_from_cart(request, item_id):
    """Remove the specified product from the cart and display a message."""
    try:
        cart = request.session.get('cart', {})
        product = get_object_or_404(Product, id=item_id)
        if item_id in cart:
            cart.pop(item_id)
            request.session['cart'] = cart

            messages.success(request, f"'{product.name}' has been removed.")
        else:
            messages.error(request, "The product was not found in your cart.")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            "An error occurred while removing the product "
            "from your cart.")
        return HttpResponse(status=500)
