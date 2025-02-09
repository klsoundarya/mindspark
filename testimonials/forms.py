from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.NumberInput(attrs={'type': 'number', 'max': '5', 'min': '1'})
    )
    class Meta:
        model = Testimonial
        fields = ['message', 'rating']
