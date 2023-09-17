from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authentications.models import User


# Register your models here.
@admin.register(User)
class CostomUserAdmin(admin.ModelAdmin):
    list_display = [
        "username", "email", "phone_number", "is_vendor", "created_at", "updated_at"
    ]
