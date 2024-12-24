from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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