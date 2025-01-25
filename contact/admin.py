from django.contrib import admin
from .models import ContactUs

# contact-admin.py


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('message', 'email', 'read')
    list_editable = ('read',)
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'name')
