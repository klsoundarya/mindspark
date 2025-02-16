from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('read/<int:pk>/', views.article_detail, name='article_detail'),
    path('read/new/', views.article_create, name='article_create'),  # Superuser only
    path('read/<int:pk>/publish/', views.publish_article, name='publish_article'),
    path('read/<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('read/<int:pk>/edit/', views.edit_article, name='edit_article'),
]
