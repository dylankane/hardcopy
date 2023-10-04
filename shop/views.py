from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Genre


def index(request):
    """ A view to return main page with products,
    including sorting and search criteria"""

    products = Product.objects.all()
    genre_list = Genre.objects.all()
    artists = Product.objects.order_by('artist').values_list(
        'artist', flat=True).distinct()
    current_artist = None
    query = None
    categories = None
    genres = None
    sort = None
    direction = None
    # artist = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            if sortkey == 'release_date':
                products = products.exclude(release_date__isnull=True)

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

        if 'artist' in request.GET:
            current_artist = request.GET['artist']
            products = products.filter(artist=current_artist)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'artists': artists,
        'current_artist': current_artist,
        'search_term': query,
        'current_categories': categories,
        'current_genres': genres,
        'genre_list': genre_list,
        'current_sorting': current_sorting,
    }
    return render(request, 'shop/index.html', context)


def product_detail(request, product_id):
    """ A view to show individual produt and its details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)
