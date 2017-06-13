from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect,render
from django.contrib import auth
from django.db import connections, connection
from general.views import get_session


def register(request):
    error = ''
    if request.method == "POST":
        login = request.POST['login']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        vchat = connections['vchat']
        bd = vchat.cursor()
        bd.execute("select login, username from users where login = '%s' and username = '%s'" % (login, username))
        res = bd.fetchone
        if res is not None:
            return HttpResponseRedirect('/invalid')
        else:
            bd.execute("insert into USERS (login, username, email, password) VALUES ('%s','%s','%s','%s')" % (login, username, email, password)) # добавление пользователя
            bd.execute("select id from users where login = '%s'" % (login))
            id = bd.fetchone()

            if id is None:
                error = 'no string'
            else:
                id = id[0]
                request.session.modefied = True
                request.session.save()
                return HttpResponseRedirect('/detail/')
    return render(request, 'registration/regform.html', {'error': error})


def detail(request):
    user = get_user(request)
    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')
    else:
        return render(request, 'registration/detail.html', user)

def get_user(request):
    id = get_session(request)
    if isinstance(id, HttpResponseRedirect):
        return id
    vchat = connections['vchat']
    bd = vchat.cursor()
    bd.execute("select id, email, username from users where id  = '%s'" % id)
    tup = bd.fetchone()
    # tup = (7, 'dsfsdf@sadasd.asdfas', 'sfsdfs')
    # user = {'id': tup[0], 'email': tup[1], 'username': tup[2]}
    user = dict(zip(('id', 'email', 'username'), tup))
    return user
