from django.urls import path
from . import views

urlpatterns = [
    path('contact_message/', views.contact_message, name='contact_message'),
]
