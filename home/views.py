from django.shortcuts import render
from testimonials.models import Testimonial
from read.models import Article

def home_view(request):
    """
    Renders the Home page with latest articles and testimonials.
    """
    latest_articles = Article.objects.filter(published=True).order_by('-created_at')[:3]
    testimonials = Testimonial.objects.all().order_by('-created_at')[:4]
    
    return render(request, 'home/home.html', {
        'latest_articles': latest_articles,
        'testimonials': testimonials
    })