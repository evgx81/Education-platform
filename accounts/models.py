from django.db import models
from django.contrib.auth.models import AbstractUser

class MLSUser(AbstractUser):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Product(models.Model):
    """
    Сущность продукта
    """

    name = models.CharField(
        verbose_name="Название продукта", 
        max_length=255, 
        unique=True
    )

    owner = models.ForeignKey(
        MLSUser, 
        verbose_name="Владелец", 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)


class Lesson(models.Model):
    """
    Сущность урока
    """

    title = models.CharField(
        verbose_name="Название урока", 
        max_length=100, 
        unique=True
    )

    url = models.URLField(verbose_name="Ссылка на видео")

    duration = models.PositiveBigIntegerField(
        verbose_name="Длительность просмотра видео"
    )

    # Уроки могут находиться в нескольких продуктах
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ("title",)


class LessonViewProgress(models.Model):
    """
    Сущность прохождения урока
    """

    user = models.ForeignKey(
        MLSUser, 
        verbose_name="Владелец", 
        on_delete=models.CASCADE
    )

    lesson = models.ForeignKey(
        Lesson, 
        verbose_name="Название урока", 
        on_delete=models.CASCADE
    )

    viewed_time = models.PositiveIntegerField(
        verbose_name="Длительность просмотра видео"
    )

    status = models.BooleanField(
        verbose_name="Статус просмотра", 
        default=False
    )

    def set_status(self):
        """
        Логика определения статуса просмотра видео
        "Просмотрено" - 1, "Не просмотрено" - 0
        """
        lesson_duration = self.lesson.duration
        if self.viewed_time >= 0.8 * lesson_duration:
            self.status = "Просмотрено"
        else:
            self.status = "Не просмотрено"
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
    
    class Meta:
        verbose_name = "Прогресс прохождения урока"
        verbose_name_plural = "Прогресс прохождения уроков"


class ProductAccess(models.Model):
    product = models.ForeignKey(
        Product, 
        verbose_name="Продукт", 
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        MLSUser, 
        verbose_name="Владелец", 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"Пользователь: {self.user.username}, Продукт: {self.product.name}"

    class Meta:
        verbose_name = "Доступ к продукту"
        verbose_name_plural = "Доступы к продуктам"
