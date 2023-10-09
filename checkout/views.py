from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        mesage.error(request, "Nothing in your cart yet!!")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': (
            'pk_test_51NqE4sKsdMEMDDI0SpNYUyLNvsPUHlB3CG3hb6hIPb94RHv5zQwxAbstKV7cICMqyiiwlFjjetejGtJAMPkftzvH00AF2I2CQZ'
            ),
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
