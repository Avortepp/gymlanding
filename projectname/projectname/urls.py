from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # Импортируем функцию static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('appname.urls')),
]

# Добавляем маршрут для статических файлов только в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)