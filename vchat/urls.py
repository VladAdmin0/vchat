from django.contrib.auth import views
from django.conf.urls import url
from django.contrib import admin, auth
import general.views, registration.views, chat.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^registration/', registration.views),
    # url(r'^chat/', chat.views),
    url(r'^$', general.views.enter),
    url(r'^invalid/', general.views.default, {"templ": "general\invalid.html"}),
    url(r'^detail/', general.views.default, {"templ": "general\detail.html"}),
]
