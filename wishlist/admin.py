from django.contrib import admin
from .models import Wishlist

class AdminWishlist(admin.ModelAdmin):
    """wishlist admin"""
    model = Wishlist
    fields = ('user', 'product', 'added_at')
    list_display = ('pk', 'user', 'product', 'added_at')


admin.site.register(Wishlist, AdminWishlist)