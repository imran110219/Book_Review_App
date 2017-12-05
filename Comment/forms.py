from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    widgets = {
      'comments': forms.Textarea(attrs={'rows':4, 'cols':110}),
    }
    fields = ('comments', 'review', )