import logging

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.forms import CustomUserCreationForm, AvatarUpdateForm

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистировались, теперь войдите в аккаунт!")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile_view(request):
    if request.method == 'POST' and request.FILES:
        form = AvatarUpdateForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                'success': True,
                'avatar_url': user.avatar.url if user.avatar else None
            })
        return JsonResponse({
            'success': False,
            'errors': form.errors.as_json()
        }, status=400)

    orders = request.user.order_set.all().order_by('-created_at')[:5]
    return render(request, 'users/profile.html', {
        'orders': orders,
    })
