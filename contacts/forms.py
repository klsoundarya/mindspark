from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):
    """
    Form for handling contact submissions.

    - Uses the Contact model to gather user input for first name,
    last name, email, subject, and message.
    - Includes custom placeholders for each field to guide the user.
    """
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

    # Customize each form field with placeholders to improve user experience
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'})
        )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '.......'})
        )
