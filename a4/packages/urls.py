from django.urls import path
from packages import views


urlpatterns = [
    path('', views.packages, name='packages'),  # Страница с ценами
]