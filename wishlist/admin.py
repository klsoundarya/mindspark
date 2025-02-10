from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class AdminWishlist(admin.ModelAdmin):
    """Wishlist admin panel configuration"""
    model = Wishlist
    fields = ('user', 'product')
    list_display = ('pk', 'user', 'product', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('user__username', 'product__name')
    ordering = ('-added_at',)
    readonly_fields = ('added_at',)
