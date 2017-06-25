from django.contrib.auth import views
from django.conf.urls import url
from django.contrib import admin, auth
import general.views, registration.views, chat.views, adressbook.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', chat.views.chat),
    url(r'^$', general.views.enter),
    url(r'^invalid/', general.views.default, {"templ": "general\invalid.html"}),
    url(r'^detail/', registration.views.detail),
    # url(r'^detail/', registration.views.detail, {"param": 'login'}),
    url(r'^registration/', registration.views.register),
    url(r'^adressbook/', adressbook.views.adressbook),
    url(r'^logout/', general.views.log_out),
    url(r'^add/', adressbook.views.add),
    url(r'^del/', adressbook.views.delete),
    # url(r'^send/', chat.views.send),
]
# (?P<id>\d+)
# (?P<id>[a-zA-Z0-9]+)