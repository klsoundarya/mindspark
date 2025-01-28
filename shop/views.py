from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import ProductForm

def all_essentials(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
    
        # Handle sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handle category filtering
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle search queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('shop'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Pagination
    paginator = Paginator(products, 12)
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
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    # Fetch related products in the same category (excluding the current product)
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id)[:4]

    # If fewer than 4 products are found, fetch additional products from other categories
    if related_products.count() < 4:
        additional_products = Product.objects.exclude(pk__in=related_products.values_list('pk', flat=True)) \
                                         .exclude(pk=product_id)[:4 - related_products.count()]
        related_products = list(related_products) + list(additional_products)

    context = {
        'product': product,
        'related_products': related_products,
    }

    return render(request, 'shop/product_detail.html', context)

def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)