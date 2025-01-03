from django.shortcuts import render

# Create your views here.

def cart_summary(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart_summary.html')