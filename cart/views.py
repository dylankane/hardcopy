from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """ A view to return a cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add item to cart with its quantity """

    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.GET.get('redirect_url')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust the cart quantity """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
