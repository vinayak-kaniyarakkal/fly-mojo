from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from django.http import HttpResponseRedirect
from img.views import get_pan_details, image_upload
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', lambda request: HttpResponseRedirect('/static/index.html')),
    url(r'^verification/$', get_pan_details),
    url(r'^upload/$', image_upload),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
