from django.db import models

# Create your models here.

# https://velog.io/@seungsang00/Database-Instagram-%EC%8A%A4%ED%82%A4%EB%A7%88-%EB%94%94%EC%9E%90%EC%9D%B8
# 위의 블로그 ERD의 users부분
class users(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_at = models.DateField()
