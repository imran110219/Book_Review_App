from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    widgets = {
      'description': forms.Textarea(attrs={'rows':6, 'cols':100}),
    }
    fields = ('description',)

    def save(self, user=None):
      review = super(ReviewForm, self).save(commit=False)
      if user:
        review.user = user
      review.save()
      return review