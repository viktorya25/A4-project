from django.db.models.signals import pre_save
from django.conf import settings
from django.dispatch import receiver
from django.core.mail import EmailMessage

from services.models import Order


@receiver(pre_save, sender=Order)
def send_payment_email_on_status_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_order = Order.objects.get(pk=instance.pk)
            if old_order.status != 'awaiting_payment' and instance.status == 'awaiting_payment':
                send_payment_email(instance)
        except Order.DoesNotExist:
            pass


def send_payment_email(order):
    subject = f'Оплата заказа на услугу "{order.service}"'
    
    body = f"""
    Здравствуйте, {order.user.username}!
    
    Ваш заказ №{order.id} на услугу "{order.service}" ожидает оплаты.
    Сумма: {order.price} руб.
    
    Оплатить: {order.get_payment_url()}
    """
    
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_HOST_USER,  # Должен совпадать с EMAIL_HOST_USER
        [order.user.email],
        reply_to=[settings.EMAIL_HOST_USER],
    )
    
    try:
        email.send(fail_silently=False)
        print(f"Письмо для заказа {order.id} отправлено!")
    except Exception as e:
        print(f"Ошибка отправки: {e}")
