from django.contrib import admin

from .models import Product, Lesson, LearningProcess, ProductAccess


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    list_filter = ("name", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "duration")


@admin.register(LearningProcess)
class LearningProcessAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "viewed_time", "status")
    readonly_fields = ("status",)


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ("product", "user")
