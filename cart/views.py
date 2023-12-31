from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from shop.models import Product


def view_cart(request):
    """ A view to display a cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add item to cart with its quantity """

    product = get_object_or_404(Product, pk=item_id)
    source = request.GET.get('source')
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(
            request,
            f'Updated <strong>{product.name.upper()}</strong> quantity\
                to <strong>{cart[item_id]}</strong>'
            )
    else:
        cart[item_id] = quantity
        messages.success(
            request,
            f'<strong>{product.name.upper() }</strong> has been\
                successfully added to the cart'
            )

    request.session['cart'] = cart

    if source == 'product_detail':
        return redirect(reverse('product_detail', args=[item_id]))

    elif source == 'shop':
        return redirect(reverse('shop'))

    elif source == 'list_of_wishes':
        return redirect(reverse('list_of_wishes'))

    else:
        return redirect(reverse('shop'))


def adjust_cart(request, item_id):
    """ Adjust the cart quantity """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated quantity of <strong>{product.name.upper()}\
                </strong> to <strong>{cart[item_id]}</strong>'
            )
    else:
        cart.pop(item_id)
        messages.success(
            request, f'<strong>{product.name.upper()}</strong> has\
                been removed from your cart'
            )

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove Items from shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        messages.success(
            request, f'<strong>{product.name.upper()}</strong> has been\
                removed from your cart'
            )

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'An error has occured removing item: {e}')
        return HttpResponse(status=500)
