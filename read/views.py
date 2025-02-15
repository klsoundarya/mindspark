from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import Article
from .forms import ArticleForm

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

@staff_member_required
def publish_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.published = True
    article.save()
    return redirect("article_detail", pk=pk)

def article_list(request):
    if request.user.is_superuser:
        articles = Article.objects.all()  # Show all (published & drafts) to superusers
    else:
        articles = Article.objects.filter(published=True)  # Only show published articles to normal users

    return render(request, "read/article_list.html", {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    # Only allow normal users to see published articles
    if not article.published and not request.user.is_superuser:
        return render(request, "404.html", status=404)  # Show 404 if user is not allowed

    return render(request, "read/article_detail.html", {"article": article})

# Function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser)  # Restrict access to superusers only
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'read/article_form.html', {'form': form})
