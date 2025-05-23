from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин',
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Имя',
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Фамилия',
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label='Почта',
    )
    avatar = forms.ImageField(required=False, label='Аватар')

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
            field.widget.attrs['placeholder'] = field.label


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
    )

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('username', 'password1')

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'input'
            field.widget.attrs['placeholder'] = field.label


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if avatar:
            if avatar.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Файл слишком большой. Максимальный размер - 5MB.")
            if not avatar.content_type.startswith('image/'):
                raise forms.ValidationError("Пожалуйста, загрузите изображение.")
        return avatar
    

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'placeholder': 'Старый пароль'}
        )
        self.fields['new_password1'].widget.attrs.update(
            {'placeholder': 'Новый пароль'}
        )
        self.fields['new_password2'].widget.attrs.update(
            {'placeholder': 'Подтвердите новый пароль'}
        )
