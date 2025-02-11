from django.contrib import messages
from django.shortcuts import render, redirect
from .models import ContactUs
from .forms import ContactForm

# Contact form handling view


def contact(request):
    """
    Handles contact form submissions and displays submitted messages for superusers.

    - If the form is submitted (POST) and valid, it saves the data and displays a success message.
    - Redirects back to the contact page after successful submission.
    - If the user is a superuser, retrieves all submitted contact messages in descending order of creation.
    - Renders the 'contact/contact.html' template with the form and contact messages (for superusers).
    """
    form = ContactForm(request.POST or None)
    contacts = ContactUs.objects.all().order_by('-created_at') if request.user.is_superuser else None  

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(
                request, "I will respond within 2 working days. Thank you for submitting the form!"
            )
            return redirect('contacts:contacts')

    return render(
        request, 'contacts/contact.html', {'form': form, 'contacts': contacts, 'is_superuser': request.user.is_superuser}
    )
