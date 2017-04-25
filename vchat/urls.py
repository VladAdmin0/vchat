from django.contrib.auth import views
from django.conf.urls import url
from django.contrib import admin, auth
import general.views, registration.views, chat.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^chat/', chat.views),
    url(r'^$', general.views.enter),
    url(r'^invalid/', general.views.default, {"templ": "general\invalid.html"}),
    url(r'^detail/(?P<id>\d+)', registration.views.detail, {"param": 'id'}),
    url(r'^detail/(?P<id>[a-zA-Z0-9]+)', registration.views.detail, {"param": 'login'}),
    url(r'^registration/', registration.views.register),
    url(r'^adressbook/(?P<id>\d+)', adressbook.views.adressbook, {"param": 'id'}),
    url(r'^adressbook/(?P<id>[a-zA-Z0-9]+)', adressbook.views.adressbook, {"param": 'login'}),
]
