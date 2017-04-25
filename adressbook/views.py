from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib import auth
from django.db import connections, connection


def adressbook(request, id, param):
    vchat = connections['vchat']
    bd = vchat.cursor()
    bd.execute("select id_ad_book, id_user from adress_book where %s = '%s'" % (param, id))
    tup = bd.fetchone()
    return render(request, 'adressbook/adbook.html', tup)
