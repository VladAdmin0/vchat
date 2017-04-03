from django.conf.urls import url
from django.contrib import admin
import general.views, registration.views, chat.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^registration/', registration.views),
    # url(r'^chat/', chat.views),
    url(r'^$', general.views.nothing, name='main'),
]
