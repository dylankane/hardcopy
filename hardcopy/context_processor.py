from newsletter.forms import NewsletterForm


def newsletter_form_processor(request):
    return {'newsletter_form': NewsletterForm()}
