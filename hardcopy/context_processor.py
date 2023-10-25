from newsletter.forms import NewsletterForm


def newsletter_form_processor(request):
    '''
    A context function to make the newsletter form availible site wide
    '''
    return {'newsletter_form': NewsletterForm()}
