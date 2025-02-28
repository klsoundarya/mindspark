from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Article
from .forms import ArticleForm

# Admin function to delete an article
@staff_member_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    messages.success(request, "The article has been successfully deleted.")
    return redirect('article_list')


# Admin function to publish an article
@staff_member_required
def publish_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.published = True
    article.save()
    messages.success(
        request, f"'{article.title}' has been "
        "published successfully!")
    return redirect("article_detail", pk=pk)

# Function to display a list of articles (all for admins, only published for users)
def article_list(request):
    if request.user.is_superuser:
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(published=True)

    return render(request, "read/article_list.html", {"articles": articles})

# Function to display article details
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if not article.published and not request.user.is_superuser:
        return render(request, "404.html", status=404)

    return render(request, "read/article_detail.html", {"article": article})

# Function to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

# Function to edit an existing article (restricted to superusers)
@login_required
@user_passes_test(is_superuser)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"The article '{article.title}' has been "
                "updated successfully.")
            return redirect("article_detail", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "read/edit_article.html", {
            "form": form, "article": article})

# Function to create a new article (restricted to superusers)
@login_required
@user_passes_test(is_superuser)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            messages.success(
                request, f"New article '{article.title}' has been "
                "created successfully.")
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'read/article_form.html', {'form': form})
