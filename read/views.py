from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Article
from .forms import ArticleForm

def article_list(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'read/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, published=True)
    return render(request, 'read/article_detail.html', {'article': article})

# Function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)  # Restrict access to superusers only
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'read/article_form.html', {'form': form})
