from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Profile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "username",
        "is_staff",
    ]
    the_fields = ()
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": the_fields}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": the_fields}),)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = [
        "id",
        "__str__",
        "skin_type",
    ]
    list_filter = ('skin_type',)
    search_fields = ('first_name',"last_name","id")
