from django.shortcuts import render

from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter(request):

    if request.method == 'POST':
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()

            messages.success(
                request,
                'You have successfully subscribed to our monthly newsletter.\
                    The newsletter will be in your inbox within \
                    the first week of every month, enjoy!!'
                )
            return render(request, 'shop/index.html')
        else:
            messages.error(
                request,
                'An error has occurred, you have not been subscribed,\
                    check if the email address in the form is valid')

    if request.method == 'GET':
        newsletter_form = NewsletterForm()

    # else:
    #     newsletter_form = NewsletterForm()
    return render(request, 'shop/index.html', {'newsletter_form': newsletter_form})

    # template = 'includes/footer.html'
    # context = {
    #     'newsletter_form': newsletter_form,
    # }
    # return render(request, template, context)
