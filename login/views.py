from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login.forms import UserForm
# Create your views here.

# def login(request):
#     return render(request, 'login/login.html')

def signup(request):
    '''
    계정생성
    '''
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)# 사용자인증
            login(request, user)
            return redirect('main')
    else:
        form = UserForm()
    return render(request, 'login/signup.html',{'form':form})


def anotherlogin(request):
    return render(request, 'login/anotherlogin.html')