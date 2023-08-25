from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class Univ(models.Model):
    univName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.univName

# 사용자 관리자 클래스 정의
class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:  # 이메일이 없을 때 오류 발생
            raise ValueError('이메일은 필수 항목입니다.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractUser):
    nickName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, unique=True)
    univ_id = models.ForeignKey(Univ, on_delete=models.CASCADE)

    objects = UserManager()

    def __str__(self):
        return self.nickName


