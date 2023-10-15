from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .models import Product, Category, Genre
from .forms import ProductForm
from reviews.models import CustomerReviews


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
    reviews = CustomerReviews.objects.filter(product=product)

    context = {
        'product': product,
        'reviews': reviews,
    }
    return render(request, 'shop/product_detail.html', context)


@login_required
def add_product(request):
    """For adding products to store """
    if not request.user.is_superuser:
        messgae.error(request, 'Sorry only staff members have access to that')
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please check the form data is correct')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """For editing products"""
    if not request.user.is_superuser:
        messgae.error(request, 'Sorry only staff members have access to that')
        return redirect(reverse('index'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Product could not be updated, \
                please check the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'you are now editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """To delete a product"""
    if not request.user.is_superuser:
        messgae.error(request, 'Sorry only staff members have access to that')
        return redirect(reverse('index'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'You have successfully deleted the product!')
    return redirect(reverse('index'))


def review_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    reviews = CustomerReviews.filter(product=product)

    context = {
        'reviews': reviews
    }
    return render(request, 'shop/product_detail.html', context)
