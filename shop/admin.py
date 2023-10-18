from django.contrib import admin
from .models import Product, Category, Genre, WishList


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'genre',
        'category',
        'price',
        'image',
    )

    list_filter = ('category', 'genre', 'artist')
    search_fields = (
        'name',
        'artist',
        'category__friendly_name',
        'genre__friendly_name'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class GenreAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class FavouritesAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(WishList, FavouritesAdmin)
