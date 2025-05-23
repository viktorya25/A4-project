from django.shortcuts import render, redirect
from django.contrib import messages

from home.forms import ApplicationForm


def home(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка успешно отправлена!')
            return redirect('home')
    else:
        form = ApplicationForm()
    
    return render(request, 'home/home.html', {'form': form})