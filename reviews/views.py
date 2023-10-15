from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from shop.models import Product
from .models import CustomerReviews
from .forms import ReviewForm


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.author = request.user
            review.save()
            messages.success(request, 'Successfully reviewed product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please check the form data is correct')
    else:
        review_form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'review_form': review_form,
        'product': product
    }

    return render(request, template, context)