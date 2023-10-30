from django.shortcuts import render, redirect, reverse

from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter(request):
    '''
    Function to handle the logic of aving the form to
    subscibe to a newsletter.
    '''
    if request.method == 'POST':
        newsletter_form = NewsletterForm(data=request.POST)

        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(
                request,
                'You have successfully subscribed to our monthly\
                    newsletter.The newsletter will be in your inbox within\
                    the first week of every month, enjoy!!')
        else:
            messages.error(
                request,
                'Email, was not added. Either not a valid email\
                    or this email already exists on our subscription list.')
        return redirect(reverse('shop'))
    else:
        newsletter_form = NewsletterForm()
        return redirect(reverse('shop'))
