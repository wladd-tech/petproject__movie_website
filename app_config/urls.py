from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from app_config import settings
from apps.main.views import custom_404


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("apps.main.urls", "apps.main"), namespace="main")),
]

handler404 = custom_404

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
