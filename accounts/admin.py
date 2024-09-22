from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'age', 'description', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)
