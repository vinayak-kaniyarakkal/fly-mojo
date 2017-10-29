from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from img.views import get_pan_details
from img.views import get_leaderboard
from django.http import HttpResponseRedirect
from img.views import image_upload
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verification/', get_pan_details),
    url(r'^leaderboard/', get_leaderboard),
    url(r'^$', lambda request: HttpResponseRedirect('/static/index.html')),
    url(r'^upload/$', image_upload),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
