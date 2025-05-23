import json
import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from yookassa.domain.notification import (
    WebhookNotificationEventType,
    WebhookNotificationFactory,
)

from services.forms import OrderForm
from services.models import Order, UserPayment


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def services_brand(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_brand')
            else:
                messages.error(
                    request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.info(
                request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь!')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-brand.html', {'form': form})


def services_prod(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_prod')
            else:
                messages.error(
                    request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.info(
                request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь.')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-prod.html', {'form': form})


def services_install(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
                messages.success(request, 'Ваша заявка успешно отправлена!')
                return redirect('services_install')
            else:
                messages.error(
                    request, 'Произошла ошибка. Пожалуйста, попробуйте ещё раз.')
        else:
            messages.info(
                request, 'Чтобы оставить заявку, пожалуйста, авторизуйтесь.')
            return redirect('login')
    else:
        form = OrderForm()

    return render(request, 'services/services-install.html', {'form': form})


def webhook(request):
    event_json = json.loads(request.body)
    logging.info(event_json)
    notification_object = WebhookNotificationFactory().create(
        event_json,
    )
    response_object = notification_object.object

    order = Order.objects.get(
        pk=response_object.metadata.get("order_id")
    )

    if (
        notification_object.event
        == WebhookNotificationEventType.PAYMENT_SUCCEEDED
    ):
        order.status = 'paid'
    elif (
        notification_object.event
        == WebhookNotificationEventType.PAYMENT_CANCELED
    ):
        order.status = 'cancelled'
    else:
        return HttpResponse(status=400)
    
    UserPayment.objects.create(
        order=order,
        user_id=order.user,
        payment_id=response_object.id,
    )

    order.save()

        
    return HttpResponse(status=200)
