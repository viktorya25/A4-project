from django import forms

from services.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service', 'description']
        widgets = {
            'service': forms.Select(attrs={
                'class': 'form-control',
                'id': 'service',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш заказ'
            }),
        }