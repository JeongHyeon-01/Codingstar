from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login/login.html')

def signup(request):
    return render(request, 'login/signup.html')

def anotherlogin(request):
    return render(request, 'login/anotherlogin.html')