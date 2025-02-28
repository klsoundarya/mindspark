from django.db import models
"""
    Model to store contact form submissions.

    Fields:
    - Name: Name of the contact person (max length: 50).
    - email: Email address of the contact person (max length: 70).
    - message: Content of the contact message.
    - created_at: Date and time when the contact message
    was created (auto set on creation).
    - read: Boolean flag indicating whether the message
    has been read by an admin (default is False).
"""


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.message}"
