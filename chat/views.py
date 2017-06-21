from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, render
from general.views import base
from registration.views import get_user


def chat(request):
    user = get_user(request)
    contact = request.path_info.replace('/chat/','')
    bd = base(request)
    if isinstance(user, HttpResponseRedirect):
        return HttpResponseRedirect('/')

    temp = {'contact': contact,
            'user': user}
    return render(request, 'chat/chat.html', temp)
