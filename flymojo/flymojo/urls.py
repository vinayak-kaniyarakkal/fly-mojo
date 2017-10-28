from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from img.views import CreateToken, image_upload, get_images
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
