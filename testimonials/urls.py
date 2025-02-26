from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
    path(
        'testimonial/delete/<int:testimonial_id>/',
        views.delete_testimonial, name='delete_testimonial'),
    path(
        'testimonial/edit/<int:testimonial_id>/',
        views.edit_testimonial, name='edit_testimonial'),
    path(
        'admin-testimonials/',
        views.admin_testimonials, name='admin_testimonials'),
]
