from django.shortcuts import render

from django.http import HttpResponse

import datetime

# Create your views here.

def test(request):
    return HttpResponse('Ted')

def test2(request):
    now = datetime.datetime.now()
    readable = "Time is {}".format(now)
    return HttpResponse(readable)