from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_essentials, name='shop'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
]