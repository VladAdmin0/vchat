from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib.sessions.models import Session
from django.db import connections, connection
from registration.views import get_user

# ses = Session.objects.get_queryset()
# s = ses.get_decoded()
# if id is not None:
#     id = request.session['id']


def adressbook(request):
    user = get_user(request)

    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')
    a = request.POST.__contains__('add')
    d = request.POST.__contains__('del')
    if a is True:
        pass




    return render(request, 'adressbook/adbook.html', user)
