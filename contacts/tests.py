from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    Test suite for ContactForm validation.

    Includes tests for required fields and form validity with valid and invalid input data.
    """

    def test_form_is_valid(self):
        """ Test for all fields """
        form = ContactForm({
            'name': 'john',
            'email': 'test@example.com',
            'subject': 'would want to get email update',
            'message': 'Hello!'
        })
        self.assertTrue(
            form.is_valid(),
            msg="ContactForm form should be valid with all fields.")

    def test_form_is_invalid(self):
        """ Test for all fields """
        form = ContactForm({
            'name': '',
            'email': '',
            'subject': '',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="ContactForm should be invalid when all fields are empty.")

    def test_name_is_required(self):
        """ Test for the 'name' field """
        form = ContactForm({
            'name': '',
            'email': 'test@example.com',
            'subject': 'would want to get email update',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """ Test for the 'email' field """
        form = ContactForm({
            'name': 'john',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """ Test for the 'message' field """
        form = ContactForm({
            'name': 'john',
            'email': 'test@example.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
