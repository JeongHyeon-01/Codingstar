from django.shortcuts import render
from rest_framework.views import APIView

from user.models import User


class Sub(APIView):
    def get (self, request):
        print('get')
        return render(request, './content/main.html')

    def post (self, request):
        print('post')
        return render(request, './content/main.html')


