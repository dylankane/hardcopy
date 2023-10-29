from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    prefix = 'newsletter_form'

    class Meta:
        model = Newsletter
        fields = (
            'email',
            )
        widgets = {
          'email': forms.EmailInput(attrs={'class': 'rounded-0'}),
        }
