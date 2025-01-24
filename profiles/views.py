from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DeletedUser
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import (
    PasswordChangeForm,
)

from .models import UserProfile, DeletedUser

@login_required
def delete_account(request):
    if request.method == "POST":
        # Delete the user and log them out
        user = request.user
        # Log the deleted user's details
        DeletedUser.objects.create(username=user.username, email=user.email)
        user.delete()
        logout(request)
        messages.success(request, "Your account has been deleted successfully.")
        return redirect('account_login')
    else:
        return render(request, 'profiles/delete_account.html')
    

@login_required
# password update
def password_update_view(request):
    """
    View to handle password updates for authenticated users.
    If the user is logged in, the form to update the password is displayed and saved.
    Displays success or error messages based on the form submission result.
    Returns:
        - A redirect to the password update page on error.
        - A redirect to the user profile update page on success.
        - A redirect to 'home' if the user is not authenticated.
    """
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = PasswordChangeForm(current_user, request.POST)

            if form.is_valid():
                form.save()

                current_user.backend = 'django.contrib.auth.backends.ModelBackend'

                messages.success(request, "Your Password Has Been Updated")
                login(request, current_user)

                return redirect('profile')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

                return redirect('password_update')
        else:
            form = PasswordChangeForm(current_user)
            return render(request, "profiles/password_update.html", {'form': form})

    else:
        messages.error(request, "Please log in to view this page!")
        return redirect('home')
    

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)