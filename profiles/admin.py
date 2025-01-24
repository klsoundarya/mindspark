from django.contrib import admin
from .models import DeletedUser
from django.contrib.auth.models import User

# Register your models here.
@admin.register(DeletedUser)
class DeletedUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'deleted_at')
    ordering = ('-deleted_at',)

# Unregister the default User model
admin.site.unregister(User)