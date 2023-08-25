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
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('슈퍼유저는 is_superuser=True 여야 합니다.')
        
        univObj = Univ.objects.get(univName = "홍익대학교")

        superuser = self.create_superuser(
            # username="admin",
            email=email,
            password=password,
            univ_id=univObj,
            **extra_fields
        )
        superuser.save()
        return superuser
    
class User(AbstractUser):
    nickName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(default='', max_length=100, null=False, unique=True)
    univ_id = models.ForeignKey(Univ, on_delete=models.CASCADE)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nickName
