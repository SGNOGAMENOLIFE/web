from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    username = models.CharField(max_length=30, null=True, blank=True, verbose_name="用户名")
    password = models.CharField(max_length=10, null=True, verbose_name="密码")
    # 用户注册时默认使用手机号码注册
    mobile = models.CharField(max_length=11, verbose_name="电话")
    gender = models.CharField(max_length=6, choices=("male", "female"), default="male", verbose_name="性别")
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username


class VerifiedCode(models.Model):
    """验证码"""
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    deleted = models.BooleanField(default=False)










