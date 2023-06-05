

# Register your models here.
from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "created_at")
    fields = ("user", "first_name", "last_name", "age" "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("first_name", "last_name")
