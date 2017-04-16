from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect,render
from django.contrib import auth
from django.db import connections, connection


def enter(request):

    # v = connections['vchat']
    # c = v.cursor()
    # c.execute('SELECT * FROM users')
    # row = c.dictfetchall()
    # with connection.cursor() as cursor:
    #     cursor.execute('SELECT * from auth_user')
    #     rows = cursor.fetchall()

    if request.method == "POST":
        login = request.POST['login']
        password = request.POST['password']
        user = auth.authenticate(username=login, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect('detail/')
        else:
            # Отображение страницы с ошибкой
            return HttpResponseRedirect('invalid/')

    return render(request, 'general\index.html')


def default(request, templ):
    return render(request, templ)
