from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from django.contrib import auth, sessions
from django.db import connections, connection


def default(request, templ):
    return render(request, templ)


def enter(request):

    if request.method == "POST":
        vchat = connections['vchat']
        bd = vchat.cursor()
        login = request.POST['login']
        password = request.POST['password']
        bd.execute("select id from users where login = '%s' and password = '%s'" % (login, password))
        res = bd.fetchone()

        if res is not None:
            id = res[0]
            request.session.modefied = True
            request.session.save()
            return HttpResponseRedirect('/detail/%s' % id)
        else:
            return HttpResponseRedirect('/invalid')

    return render(request, 'general\index.html')

    # v = connections['vchat']
    # c = v.cursor()
    # c.execute('SELECT * FROM users')
    # row = c.dictfetchall()
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * from auth_user')
    #     rows = cursor.fetchall()

# bd.execute("insert into USERS (login, username, email, password) VALUES ('%s','%s','%s','%s')" % (
# login, username, email, password))
# user = auth.authenticate(username=login, password=password)
# if user is not None and user.is_active:
#     # Правильный пароль и пользователь "активен"
#     auth.login(request, user)
#     # Перенаправление на "правильную" страницу
#     return HttpResponseRedirect('detail/(?P<id>\d+)')
# else:
#     # Отображение страницы с ошибкой
#     return HttpResponseRedirect('invalid/')

