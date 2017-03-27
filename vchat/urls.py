from django.conf.urls import url
from django.contrib import admin
# from general.models import *
# from registration.models import *
import general
import registration

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^registration/', ????),
    # url(r'^chat/', chat.urls),
    # url(r'^main/', general.urls),
]
