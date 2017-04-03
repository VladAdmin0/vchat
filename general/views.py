from django.shortcuts import render_to_response
from django.http import HttpResponse
from general.models import RegWindow


def nothing(reguest):
    name_list = RegWindow.objects.all()
    pass_list = RegWindow.objects.all()
    return render_to_response('general/base.html', {'login': name_list, 'password': pass_list})
