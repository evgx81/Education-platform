from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import MLSUser


class Product(models.Model):
    """
    Продукт
    """

    name = models.CharField(
        verbose_name=_("Название продукта"), max_length=255, unique=True
    )

    owner = models.ForeignKey(
        MLSUser, verbose_name=_("Владелец"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Продукт")
        verbose_name_plural = _("Продукты")
        ordering = ("name",)


class Lesson(models.Model):
    """
    Урок
    """

    title = models.CharField(
        verbose_name=_("Название урока"), max_length=100, unique=True
    )

    url = models.URLField(verbose_name=_("Ссылка на видео"))

    duration = models.PositiveBigIntegerField(
        verbose_name=_("Длительность просмотра видео")
    )

    # Уроки могут находиться в нескольких продуктах
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _("Урок")
        verbose_name_plural = _("Уроки")
        ordering = ("title",)


class LearningProcess(models.Model):
    """
    Прохождение обучения
    """

    class ViewedStatus(models.IntegerChoices):
        """Статус просмотра"""

        NOT_VIEWED = 0, _("Не просмотрено")
        VIEWED = 1, _("Просмотрено")

    user = models.ForeignKey(
        MLSUser, verbose_name=_("Студент"), on_delete=models.CASCADE
    )

    lesson = models.ForeignKey(
        Lesson, verbose_name=_("Название урока"), on_delete=models.CASCADE
    )

    viewed_time = models.PositiveIntegerField(
        verbose_name=_("Длительность просмотра видео"), default=0
    )

    status = models.IntegerField(
        verbose_name=_("Статус просмотра"),
        choices=ViewedStatus.choices,
        default=ViewedStatus.NOT_VIEWED,
    )

    def save(self, *args, **kwargs):
        """
        Логика определения статуса просмотра видео
        "Просмотрено" - 1, "Не просмотрено" - 0
        """
        lesson_duration = self.lesson.duration
        self.status = (
            self.ViewedStatus.VIEWED
            if self.viewed_time >= 0.8 * lesson_duration
            else self.ViewedStatus.NOT_VIEWED
        )
        super(LearningProcess, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title},  {self.status}"

    class Meta:
        verbose_name = _("Прогресс прохождения урока")
        verbose_name_plural = _("Прогресс прохождения уроков")


class ProductAccess(models.Model):
    """
    Доступы пользователей к продуктам
    """

    product = models.ForeignKey(
        Product, verbose_name=_("Продукт"), on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        MLSUser, verbose_name=_("Студент"), on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"Пользователь: {self.user.username}, Продукт: {self.product.name}"

    class Meta:
        verbose_name = _("Доступ к продукту")
        verbose_name_plural = _("Доступы к продуктам")
        unique_together = ("product", "user")
