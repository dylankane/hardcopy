from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    """ A view to return main page with products,
    including sorting and search criteria"""

    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    """ A view to show individual produt and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)
