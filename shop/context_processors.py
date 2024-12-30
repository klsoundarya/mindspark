from .models import Category

def global_categories(request):
    """Provide all categories globally."""
    categories = Category.objects.all()
    return {'all_categories': categories}
