from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    widgets = {
      'review_description': forms.Textarea(attrs={'rows':6, 'cols':100}),
    }
    fields = ('review_description',)