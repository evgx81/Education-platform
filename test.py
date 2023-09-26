from django.db import models


class ViewedStatus(models.IntegerChoices):
    """Статус просмотра"""

    NOT_VIEWED = 0, "Не просмотрено"
    VIEWED = 1, "Просмотрено"


choices = ViewedStatus.NOT_VIEWED
print(ViewedStatus.choices)
