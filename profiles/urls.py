from django.urls import path
from . import views

urlpatterns = [
    path('profiles/delete/', views.delete_account, name='delete_account'),
    path('', views.profile, name='profile')
]