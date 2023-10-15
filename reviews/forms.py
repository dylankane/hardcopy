from django import forms
from .models import CustomerReviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CustomerReviews
        fields = (
            'body',
            'rating',
            )
