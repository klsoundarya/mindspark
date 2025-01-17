from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]