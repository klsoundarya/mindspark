from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Testimonial
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm

@login_required
def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    # Ensure the testimonial belongs to the logged-in user or is anonymous
    if testimonial.user == request.user or testimonial.user is None:
        testimonial.delete()
        messages.success(request, "Testimonial deleted successfully.")
    else:
        messages.error(request, "You can only delete your own testimonials.")

    return redirect('home')

@login_required
def edit_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    # Ensure the testimonial belongs to the logged-in user
    if testimonial.user != request.user:
        messages.error(request, "You can only edit your own testimonials.")
        return redirect('home')

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial updated successfully.")
            return redirect('home')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'testimonials/edit_testimonial.html', {'form': form})

@login_required
def submit_testimonial(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user  # Assigning logged-in user
            testimonial.save()
            messages.success(request, "Your testimonial has been submitted.")
            return redirect('home')
    else:
        form = TestimonialForm()
    
    return render(request, 'testimonials/submit_testimonial.html', {'form': form})

def display_testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')[:4]
    return render(request, 'testimonials/testimonials_section.html', {'testimonials': testimonials})
