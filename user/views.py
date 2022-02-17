import os
from uuid import uuid4

from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response

from codingsta.settings import MEDIA_ROOT
from .models import User
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password


class Signup(APIView):
    def get(self, request):
        return render(request, './user/signup.html')

    def post(self, request):
        # 회원가입
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email, nickname=nickname, name=name, password=make_password(password),
                            profile_img='defult_profile_img.jpg')

        return HttpResponseRedirect(reverse('user:signin'))


class Signin(APIView):
    def get(self, request):
        return render(request, "./user/signin.html")

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # 로그인
        user = User.objects.filter(email=email).first()

        if user is None:
            return RuntimeError(400)

        if user.check_password(password):
            #로그인을 했다. 세션 or 쿠키
            request.session['email'] = email
            return HttpResponseRedirect(reverse('content:main'))
        else:
            return HttpResponse("에러")


def logout(request):
    auth.logout(request)
    return redirect('user:signin')


class UpdateProfile(APIView):
    def post(self,request):
        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name
        email = request.data.get('email')

        user=User.objects.filter(email=email).first()
        user.profile_img = profile_image
        user.save()

        return Response(status=200)