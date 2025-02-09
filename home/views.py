from django.shortcuts import render
from testimonials.models import Testimonial

def home_view(request):
    """
    Renders the Home page
    """
    testimonials = Testimonial.objects.all().order_by('-created_at')[:4]
    return render(request, 'home/home.html', {'testimonials': testimonials})
