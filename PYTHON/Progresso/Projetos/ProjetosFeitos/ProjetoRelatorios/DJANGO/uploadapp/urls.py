from django.urls import path
from .views import upload_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', upload_view, name='upload_form'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)