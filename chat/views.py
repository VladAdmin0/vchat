from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from general.views import base
from registration.views import get_user
from datetime import datetime

def get_id_contact(request, temp):
    bd = base(request)
    cont = temp['contact']
    bd.execute("select id from users where login = '%s'" % (cont))
    id_cont = bd.fetchone()[0]
    id = temp['user']['id']
    return id_cont, id



def chat(request):
    user = get_user(request)
    contact = request.path_info.replace('/chat/','')
    bd = base(request)
    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')

    temp = {'contact': contact,
            'user': user}
    id_cont = get_id_contact(request, temp)[0]
    id = user['id']
    # texts = {}
    bd.execute("select text, send_at from messages where id_sender = '%s' AND id_recipient = '%s'" % (id, id_cont))
    if bd.rowcount > 0:
        t = []
        for x, y in bd.fetchall():
            t.append(str(x) + '   ' + str(y))
        temp['id'] = t
        # temp.update(texts)
    bd.execute("select text, send_at from messages where id_sender = '%s' AND id_recipient = '%s'" % (id_cont, id))
    if bd.rowcount > 0:
        t = []
        for x, y in bd.fetchall():
            t.append(str(x) + '   ' + str(y))
        temp['id_cont'] = t
        # temp.update(texts)
    if request.method == 'POST':
        text = request.POST['sender']
        d = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        if text != '':
            bd.execute("insert into messages (id_sender, id_recipient, send_at, text) VALUES ('%s', '%s', '%s', '%s')" % (
        id, id_cont, d, text))
            return HttpResponseRedirect('/chat/%s' % temp['contact'])
    # request.POST['hist'] = texts
    return render(request, 'chat/chat.html', temp)


# def send(request):
    # bd = base(request)
    # s = get_id_contact(request)[1]
    # r = get_id_contact(request)[0]
    # d = datetime.now()
    # login = chat(request)['temp']['contact']
    # text = request.POST['sender']
    # bd.execute("insert into messages (id_sender, id_recipient, send_at, text) VALUES ('%s', '%s', '%s', '%s')" % (s, r, d, text))
    # return HttpResponseRedirect('/chat/%s'% login)


