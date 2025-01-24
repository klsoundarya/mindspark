from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _

class PasswordChangeForm(SetPasswordForm):
    """
    Form to handle password change for the user.
    Validates the new password according to specific criteria and updates the user's password.
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
            "<li>Your password can’t be too similar to your other personal information.</li>"
            "<li>Your password must contain at least 8 characters.</li>"
            "<li>Your password can’t be a commonly used password.</li>"
            "<li>Your password can’t be entirely numeric.</li>"
            "</ul>"
        )

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = (
            "<ul><li>Enter the same password as before, for verification.</li></ul>"

        )
