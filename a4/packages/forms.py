from django import forms
from services.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service', 'price']
        widgets = {
            'service': forms.HiddenInput(),
            'price': forms.HiddenInput(),
        }