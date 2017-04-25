from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect,render
from django.contrib import auth
from django.db import connections, connection


def register(request):
    error = ''
    if request.method == "POST":
        login = request.POST['login']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        vchat = connections['vchat']
        bd = vchat.cursor()
        bd.execute("insert into USERS (login, username, email, password) VALUES ('%s','%s','%s','%s')" % (login, username, email, password))
        bd.execute("select id from users where login = '%s'" % (login))
        id = bd.fetchone()

        if id is None:
            error = 'no string'
        else:
            id = id[0]
            request.session.modefied = True
            request.session.save()
            return HttpResponseRedirect('/detail/%s' % id)
    return render(request, 'registration/regform.html', {'error': error})


def detail(request, id, param):
    vchat = connections['vchat']
    bd = vchat.cursor()
    bd.execute("select id, email, username from users where %s = '%s'" % (param, id))
    tup = bd.fetchone()
    # tup = (7, 'dsfsdf@sadasd.asdfas', 'sfsdfs')
    # user = {'id': tup[0], 'email': tup[1], 'username': tup[2]}
    user = dict(zip(('id', 'email', 'username'), tup))
    return render(request, 'registration/detail.html', user)
