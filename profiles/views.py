from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DeletedUser
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import (
    PasswordChangeForm,
    UserProfileForm
)
from checkout.models import Order

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


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)