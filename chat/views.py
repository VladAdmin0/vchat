from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib import auth
from django.db import connections, connection
from registration.views import get_user


def chat(request):
    user = get_user(request)
    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')
    else:
        return render(request, 'chat/chat.html', user)
