from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib.sessions.models import Session
from django.db import connections, connection

# ses = Session.objects.get_queryset()
# s = ses.get_decoded()


def adressbook(request):

    if id is not None:
        id = request.session['id']
    return render(request, 'adressbook/adbook.html')
