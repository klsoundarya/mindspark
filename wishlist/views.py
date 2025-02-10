from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wishlist
from shop.models import Product

@login_required
def wishlist_view(request):
    """Display the user's wishlist."""
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, "wishlist/wishlist.html", {"wishlist_items": wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    """Add a product to the user's wishlist."""
    product = get_object_or_404(Product, pk=product_id)

    if Wishlist.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, f'{product.name} is already in your Wishlist.')
    else:
        Wishlist.objects.create(user=request.user, product=product)
        messages.success(request, f'{product.name} added to Wishlist!')

    # Redirect to the product detail page
    return redirect(reverse('product_detail', args=[product_id]))

@login_required
def remove_from_wishlist(request, product_id):
    """Remove a product from the user's wishlist."""
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, f"'{product.name}' removed from your wishlist.")
    else:
        messages.error(request, f"'{product.name}' was not in your wishlist.")

    return redirect(reverse('wishlist'))
