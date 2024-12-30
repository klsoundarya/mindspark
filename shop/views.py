from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def all_essentials(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None

    # Handle category filtering
    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    # Handle search queries
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # Pagination
    paginator = Paginator(products, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    paginated_products = paginator.get_page(page_number)

    # Adding ratings to display
    for product in paginated_products:
        if product.rating:
            product.display_rating = round(product.rating * 2) / 2
        else:
            product.display_rating = None

    context = {
        'products': paginated_products,
        'search_term': query,
        'current_categories': categories,
        'all_categories': Category.objects.all(),
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