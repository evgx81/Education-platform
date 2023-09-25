from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MLSUserChangeForm, MLSUserCreationForm
from .models import MLSUser

from .models import Product, Lesson, LessonViewProgress, ProductAccess

MLSUser = get_user_model()


class MLSUserAdmin(UserAdmin):
    add_form = MLSUserCreationForm
    form = MLSUserChangeForm
    model = MLSUser
    list_display = (
        "email",
        "username",
    )

admin.site.register(MLSUser, MLSUserAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    list_filter = ("name", "owner")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "duration")


@admin.register(LessonViewProgress)
class LessonViewProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "viewed_time", "status")


@admin.register(ProductAccess)
class ProductAccessAdmin(admin.ModelAdmin):
    list_display = ("product", "user")
