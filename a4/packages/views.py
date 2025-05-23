from django.shortcuts import render, redirect
from django.contrib import messages
from packages.forms import OrderForm


def packages(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('packages')
            else:
                messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.info(request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь!')
            return redirect('login')
    else:
        form = OrderForm()
    
    return render(request, 'packages/packages.html', {'form': form})