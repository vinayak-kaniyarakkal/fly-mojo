from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
