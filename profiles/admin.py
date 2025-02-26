from django.contrib import admin
from .models import DeletedUser, Faq
from django.contrib.auth.models import User


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('question', 'answer')


# Register your models here.
@admin.register(DeletedUser)
class DeletedUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'deleted_at')
    ordering = ('-deleted_at',)


# Unregister the default User model
admin.site.unregister(User)
