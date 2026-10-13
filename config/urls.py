from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Custom 403 Error Page
handler403 = "blog.views.custom_403"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]

# Media files
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
