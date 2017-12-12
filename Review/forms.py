from django import forms

from .models import Review

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    widgets = {
      'review_description': forms.Textarea(attrs={'rows':6, 'cols':100}),
    }
    fields = ('review_description',)

    def save(self, user=None):
      review = super(ReviewForm, self).save(commit=False)
      if user:
        review.user = user
      review.save()
      return review