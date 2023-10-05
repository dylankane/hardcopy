from django.shortcuts import render


def view_cart(request):
    """ A view to return a cart page """

    return render(request, 'cart/cart.html')
