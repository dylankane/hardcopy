from django.contrib import admin
from .models import CustomerReviews


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'body',
        'rating',
        'created_on',
        'author',
    )


admin.site.register(CustomerReviews, ReviewAdmin)
