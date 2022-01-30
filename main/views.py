from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Main_feed(request):
    return HttpResponse('Here is main feed page')