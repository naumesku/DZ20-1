from django.contrib.auth.models import AbstractUser
from django.db import models

from product.models import NULLABLE


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=30, verbose_name='страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='активация пользователя')
    token = models.CharField(max_length=300, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


