from django.urls import path
from projects import views

urlpatterns = [
    path('', views.index, name='projects'),  # Страница с проектами
    path('generate-image/', views.generate_image, name='generate_image'),
]