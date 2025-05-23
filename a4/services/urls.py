from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from services import views


urlpatterns = [
    path('branding/', views.services_brand, name='services_brand'),  # Страница с Брендингом
    path('production/', views.services_prod, name='services_prod'),  # Страница с Производством
    path('installation/', views.services_install, name='services_install'),  # Страница с Установкой
    path('yookassa-webhook/', csrf_exempt(views.webhook), name='yookassa_webhook'),
]