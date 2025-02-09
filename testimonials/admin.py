from django.contrib import admin
from django import forms
from django.forms import NumberInput
from .models import Testimonial

class TestimonialAdminForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'
        widgets = {
            'rating': NumberInput(attrs={'min': 1, 'max': 5})
        }

    def clean_rating(self):
        rating = self.cleaned_data.get("rating")
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    form = TestimonialAdminForm  # Use the custom form
    list_display = ('user', 'rating', 'created_at')
    search_fields = ('user__username', 'message')
    list_filter = ('rating', 'created_at')
    ordering = ('-created_at',)
