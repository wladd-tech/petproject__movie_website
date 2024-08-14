from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from apps.main.views import page_not_found

from app_config import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(("apps.main.urls", "apps.main"), namespace='main')),
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)