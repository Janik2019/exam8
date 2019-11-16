from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'raiting']