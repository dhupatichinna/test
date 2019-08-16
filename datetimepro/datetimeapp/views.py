from django.shortcuts import render
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()

def datetime_view(request):
    d="<h1> The Current Date And Time Is:{}</h1>".format(date1)
    return HttpResponse(d)