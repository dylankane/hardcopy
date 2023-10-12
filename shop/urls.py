from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
]
