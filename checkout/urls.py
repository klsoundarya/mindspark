from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('wh/', webhook, name='webhook'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
]