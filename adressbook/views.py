from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from registration.views import get_user
from general.views import base


def adressbook(request):
    user = get_user(request)
    id = user['id']

    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')
    bd = base(request)

    # вывод всех контактов из адресной книги
    bd.execute("select id, contact_id from contacts WHERE id_user = '%s'" % (id))
    logins = []
    if bd.rowcount > 0:

        contact_ids = []
        for c in bd.fetchall():
            contact_ids.append(str(c[1]))
        bd.execute("select id, login from users WHERE id IN (%s)" % (','.join(contact_ids)))
        for c in bd.fetchall():
            logins.append(str(c[1]))
        # for i in cont:
        #     bd.execute("select login from users WHERE id = '%s'" % (i))
        #     login = bd.fetchone()
        #     logins += login
        # res = dict(zip((cont), logins))
        # conts = ()
        # for i in cont:
        #     conts += i
    template_params = {
        'user': user,
        'logins': logins
    }

    return render(request, 'adressbook/adbook.html', template_params)


# Add User
def add(request):
    user = get_user(request)
    id = user['id']
    bd = base(request)
    a = request.POST.__contains__('add')
    if a is True:
        ad = request.POST['add_contact']
        if ad is not None:
            bd.execute("select id from users where login = '%s'" % (ad)) # проверка на наличие логина в базе
            contact_id = bd.fetchone()[0]
            if contact_id is not None:
                bd.execute("insert into contacts (contact_id, id_user) VALUES ('%s', '%s')" % (contact_id, id)) # добавление пользователя

    return HttpResponseRedirect('/adressbook/')


# Delete User
def delete(request):
    user = get_user(request)
    id = user['id']
    bd = base(request)
    d = request.POST.__contains__('del')
    if d is True:
        de = request.POST['del_contact']
        if de is not None:
            bd.execute("select id from users where login = '%s'" % (de)) # проверка на наличие логина в базе
            del_id = bd.fetchone()[0]
            if del_id is not None:
                bd.execute("select id, contact_id, id_user from contacts where contact_id = '%s' AND id_user = '%s'" % (del_id, id)) # проверка на наличие контакта в адресной книге пользователя
                if bd.rowcount > 0:
                    id = bd.fetchone()[0]
                    bd.execute("DELETE FROM contacts WHERE id = '%s'" % (id))

    return HttpResponseRedirect('/adressbook/')