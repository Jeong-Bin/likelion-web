from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager 
# Create your models here.


# class customer_information(models.Model):
#     email = models.CharField('이메일', max_length=200)
#     password = models.TextField('암호', blank=True)
#     created_at = models.DateTimeField('생성날짜', auto_now_add=True)  # 생성될때 픽스됨
#     modified_at = models.DateTimeField('수정날짜', auto_now=True)  # 수정할때마다 바뀜

#     def __str__(self):
#         return self.title

# class UserManager(BaseUserManager):
#     def create_superuser(self, *args, **kwargs):
#         return super().create_superuser(age=30, *args, **kwargs)



class User(AbstractUser):
    # objects = UserManager()
    pass


