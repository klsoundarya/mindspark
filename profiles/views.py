from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import DeletedUser
from django.contrib.auth import logout
from django.contrib import messages

from .models import UserProfile

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
    

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)