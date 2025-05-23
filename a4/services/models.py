from django.db import models
from django.conf import settings

from yookassa import Configuration, Payment


class Order(models.Model):
    STATUS_CHOICES = [
        ('discussion', 'Обсуждение'),
        ('development', 'Проработка'),
        ('in_progress', 'В процессе'),
        ('review', 'Проверка'),
        ('awaiting_payment', 'Ожидание оплаты'),
        ('paid', 'Оплачено'),
        ('frozen', 'Заморожено'),
        ('cancelled', 'Отменено'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    service = models.CharField(max_length=255, verbose_name="Услуга")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата начала")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Цена"
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='discussion',
        verbose_name="Статус"
    )
    completion_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата окончания"
    )
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return f"Заказ от пользователя {self.user.username} на {self.service}"


    def get_payment_url(self):
        Configuration.account_id = settings.YOOKASSA_SHOP_ID
        Configuration.secret_key = settings.YOOKASSA_SECRET_KEY
        
        payment = Payment.create({
            "amount": {
                "value": str(self.price),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": settings.YOOKASSA_RETURN_URL
            },
            "capture": True,
            "description": f"Оплата заказа на услугу {self.service} (ID: {self.id})",
            "metadata": {
                "order_id": self.id,
                "user_id": self.user.id
            }
        })
        
        return payment.confirmation.confirmation_url

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class UserPayment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Платёж {self.payment_id} для заказа {self.order.id}"
