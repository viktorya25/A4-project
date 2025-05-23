from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path('packages/', include('packages.urls')),
    path('reviews/', include('reviews.urls')),
    path('services/', include('services.urls')),
    path('users/', include('users.urls')),
]

if settings.MEDIA_ROOT:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=(settings.MEDIA_ROOT),
    )