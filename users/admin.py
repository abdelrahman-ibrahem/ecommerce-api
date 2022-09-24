from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustonAdminPage(admin.ModelAdmin):
    list_display = [
            'username', 'email', 'role'
        ]
