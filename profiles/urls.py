from django.urls import path
from . import views

urlpatterns = [
    path('password_update/', views.password_update_view, name='password_update'),
    path('profiles/delete/', views.delete_account, name='delete_account'),
    path('', views.profile, name='profile')
]