from django.urls import path
from . import views

urlpatterns = [
    path('password_update/', views.password_update_view, name='password_update'),
    path('profiles/delete/', views.delete_account, name='delete_account'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('', views.profile, name='profile')
]