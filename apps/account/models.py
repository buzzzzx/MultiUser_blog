from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    """扩展user模型"""
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='female')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", max_length=100)

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name="验证码类型", max_length=20, choices=(('register', u"注册"), ('forget', u"找回密码")))
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")  # 把括号去掉，这个时间就是这个class实例化的时间

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)
