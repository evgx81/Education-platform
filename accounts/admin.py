from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MLSUserChangeForm, MLSUserCreationForm
from .models import MLSUser


MLSUser = get_user_model()


class MLSUserAdmin(UserAdmin):
    add_form = MLSUserCreationForm
    form = MLSUserChangeForm
    model = MLSUser
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
    )


admin.site.register(MLSUser, MLSUserAdmin)
