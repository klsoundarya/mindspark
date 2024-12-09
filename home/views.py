from django.shortcuts import render

def home_view(request):
    """
    Renders the Home page
    """
    return render(request, 'home/home.html')
