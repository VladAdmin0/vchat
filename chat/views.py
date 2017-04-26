from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib import auth
from django.db import connections, connection


def chat(request):
    # vchat = connections['vchat']
    # bd = vchat.cursor()
    # bd.execute("select id, email, username from users where %s = '%s'" % (param, id))
    # tup = bd.fetchone()
    # user = dict(zip(('id', 'email', 'username'), tup))
    return render(request, 'chat/chat.html')
