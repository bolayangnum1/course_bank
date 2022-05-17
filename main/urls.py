from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from . import settings
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('course.urls')),
    path(r'', include('data.urls')),
    path(r'', include('topik.urls')),
    path(r'', include('data.urls')),
    path(r'', include('test.urls')),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'', include('djoser.urls')),
    re_path(r'', include('djoser.urls.jwt')),
    path('', include('account.urls'))
]

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

