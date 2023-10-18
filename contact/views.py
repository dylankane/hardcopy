from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact_message(request):
    """
    A function to render contact page,
    provide contact form
    """
    if request.user.is_authenticated:
        user = request.user
        email = request.user.email
        contact_form = ContactForm(initial={'email': email})

        if request.method == 'POST':
            contact_form = ContactForm(data=request.POST)

            if contact_form.is_valid():
                contact = contact_form.save(commit=False)
                contact.author = user
                contact.save()
                messages.success(request, 'Successfully sent message')

                return render(request, 'shop/index.html')

            else:
                messages.error(
                    request,
                    'Message could not be sent check the data in the form')

    else:
        messages.error(
                    request,
                    'You must be logged in to send us a messge here.\
                         If you want to contact us my email feel free')

    template = 'contact/contact_message.html'
    context = {
        'contact_form': contact_form,
        'user': user
    }
    return render(request, template, context)
