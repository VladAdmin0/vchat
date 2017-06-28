from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from general.views import base
from registration.views import get_user
from datetime import datetime


def get_id_contact(request, cont):
    bd = base(request)
    bd.execute("select id from users where login = '%s'" % (cont))
    id_cont = bd.fetchone()[0]
    return id_cont



def chat(request):
    user = get_user(request)
    contact = request.path_info.replace('/chat/','')
    bd = base(request)
    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')
    messages = {}
    id_cont = get_id_contact(request, contact)
    id = user['id']
    user_logins = {id: user['username'],
                   id_cont: contact}
    temp = {'contact': contact,
            'user': user,
            'mes': messages,
            'logins': user_logins}
    ids = (','.join(map(str, (id, id_cont))))
    bd.execute("select id_mes, id_sender, id_recipient, text, send_at from messages where id_sender IN (%s) AND "
               "id_recipient IN (%s) ORDER BY send_at" % (ids, ids))
    if bd.rowcount > 0:
        for item in bd.fetchall():
            item = dict(zip(('id', 'sender', 'recipient',  'text', 'send'), item))
            item['send'] = item['send'].strftime("%H:%M:%S %d.%m.%Y")
            item['login'] = user_logins[item['sender']]
            messages[item['id']] = item
    if request.method == 'POST':
        text = request.POST['sender']
        d = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
        if text != '':
            bd.execute("insert into messages (id_sender, id_recipient, send_at, text) VALUES ('%s', '%s', '%s', '%s')" % (
        id, id_cont, d, text))
            return HttpResponseRedirect('/chat/%s' % temp['contact'])
    return render(request, 'chat/chat.html', temp)



