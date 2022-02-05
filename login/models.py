from django.db import models

# Create your models here.

# https://velog.io/@seungsang00/Database-Instagram-%EC%8A%A4%ED%82%A4%EB%A7%88-%EB%94%94%EC%9E%90%EC%9D%B8
# 위의 블로그 ERD의 users부분
class users(models.Model):
    user = models.CharField(max_length=100, unique = True,primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique = True, null =True)
    phone_number = models.CharField(max_length=100, unique = True, null = True)
    password = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add = True)
    update_at = models.DateField(auto_now = True)
