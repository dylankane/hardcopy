from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class CustomerReviews(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='review')
    body = models.TextField()
    rating = models.IntegerField(default=5)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Review {self.rating} {self.body} by {self.author}"
