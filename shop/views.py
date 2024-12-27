from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_essentials(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    for product in products:
        if product.rating:
            product.display_rating = round(product.rating * 2) / 2
        else:
            product.display_rating = None

    context = {
        'products': products,
    }

    return render(request, 'shop/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    # Fetch related products in the same category (excluding the current product)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'shop/product_detail.html', context)