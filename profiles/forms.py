from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import UserProfile


class PasswordChangeForm(SetPasswordForm):
    """
    Form to handle password change for the user.
    Validates the new password according to specific
    criteria and updates the user's password.
    Fields:
        - new_password1: The new password.
        - new_password2: Confirmation of the new password.
    """
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = (
            "<ul>"
            + "<li>Your password can’t be too similar to your"
            + " other personal information.</li>"
            + "<li>Your password must contain at least 8 characters.</li>"
            + "<li>Your password can’t be a commonly used password.</li>"
            + "<li>Your password can’t be entirely numeric.</li>"
            + "</ul>"
        )

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = (
            'Confirm Password')
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = (
            "<ul><li>Enter the same password as before, for "
            "verification.</li></ul>"
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black rounded-0 profile-form-input')

            self.fields[field].label = False
