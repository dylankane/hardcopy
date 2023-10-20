from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path(
        'edit_product/<int:product_id>/',
        views.edit_product,
        name='edit_product'),
    path(
        'delete_product/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path(
        'wish_list/<int:product_id>/',
        views.wish_list,
        name='wish_list'),
    path(
        'list_of_wishes/',
        views.list_of_wishes,
        name='list_of_wishes'),
    path(
        'about/',
        views.about,
        name='about'),
]
