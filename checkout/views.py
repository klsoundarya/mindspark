from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QhycN2KQX7k6PHcf7dKeBZn73Fsk1CZJW5ZwWQeZcK6YZJZ14s4UF9kpK4fl7TM5vwFreV0ZKgyETA87aRcNAi100YWSglePl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)