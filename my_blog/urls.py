from django.conf import settings

from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
urlpatterns = [
    path("", include("pinax.blog.urls", namespace="pinax_blog")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
