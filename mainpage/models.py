from django.db import models


class RegWindow(models.Model):

    login = models.CharField(max_length=30, unique=True, verbose_name='Логин')
    password = models.CharField(max_length=30, verbose_name='Пароль')
