from django import forms
from reviews.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'review_input',
                'placeholder': 'Напишите отзыв',
                'required': True,
            }),
            'author': forms.HiddenInput(),
        }