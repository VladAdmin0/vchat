from django.db import models


class Reg(models.Model):

    login = models.CharField(max_length=30, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=30, verbose_name='Пароль')
    conf_password = models.CharField(max_length=30, verbose_name='Пароль')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Почта')




