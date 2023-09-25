from rest_framework import serializers
from ..accounts.models import Product, Lesson, LessonViewProgress, ProductAccess

class ProductSerializer(serializers.ModelSerializer):
    """
    Сереализатор для продуктов
    """
    class Meta:
        model = Product
        fields = '__all__'

    