from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _


class MLSUser(AbstractUser):
    """
    Пользователь системы обучения
    """

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
