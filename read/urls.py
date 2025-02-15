from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.article_list, name='article_list'),
    path('blog/<int:pk>/', views.article_detail, name='article_detail'),
    path('blog/new/', views.article_create, name='article_create'),  # Superuser only
]
