from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def index(request):
    """ A view to return main page with products,
    including sorting and search criteria"""

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered")
                return redirect(reverse('shop'))

            queries = Q(
                name__icontains=query
                ) | Q(
                description__icontains=query
                ) | Q(
                artist__icontains=query
                ) | Q(
                release_date__icontains=query
                )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    """ A view to show individual produt and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)
