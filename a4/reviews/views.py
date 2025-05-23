from django.shortcuts import render, redirect
from django.contrib import messages

from reviews.models import Review
from reviews.forms import ReviewForm


def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            messages.success(request, 'Спасибо за ваш отзыв!')
            return redirect('reviews')
        else:
            messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
    else:
        form = ReviewForm()

    all_reviews = Review.objects.all().order_by('-created_at')

    return render(request, 'reviews/reviews.html', {
        'form': form,
        'reviews': all_reviews,
    })