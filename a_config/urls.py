from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from a_config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app_page.urls")),
    path("accounts/", include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
