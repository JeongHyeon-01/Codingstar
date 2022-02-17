from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.
class User(AbstractBaseUser):
    '''
        프로필 사진
        유저 아이디 - > 화면표기이름(닉네임)
        유저 이름 -> 실제사용자이름
        유저 이메일 - >회원가입시 사용하는 아이디
        유저 비밀번호 ->디폴트 이용
    '''

    profile_img = models.TextField()
    nickname = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'nickname'

    class Meta:
        db_table = 'User'