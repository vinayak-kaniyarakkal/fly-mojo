from django.conf.urls import url
from django.contrib import admin
from django.views.static import serve
from img.views import get_pan_details
from img.views import get_leaderboard
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^verification/', get_pan_details),
    url(r'^leaderboard/', get_leaderboard),

    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
