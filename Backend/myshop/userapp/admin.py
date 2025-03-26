# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'email', 'role', 'is_email_verified', 'is_active')
#     list_filter = ('role', 'is_email_verified', 'is_active')
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role', 'profile_picture', 'is_email_verified', 'otp_secret')}),
#     )

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, LoginAttempt

class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ['email']
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active', 'is_email_verified', 'created_at')
    list_filter = ('role', 'is_staff', 'is_active', 'is_email_verified')
    
    fieldsets = (
        (_("Personal Info"), {"fields": ("email", "password", "first_name", "last_name", "profile_picture")}),
        (_("Permissions"), {"fields": ("role", "is_staff", "is_superuser", "is_active")}),
        (_("Security"), {"fields": ("is_email_verified", "otp_secret")}),
        (_("Important dates"), {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name", "last_name", "role", "is_staff", "is_active"),
        }),
    )

    search_fields = ("email", "first_name", "last_name")
    readonly_fields = ("last_login", "created_at", "updated_at")

admin.site.register(User, UserAdmin)


class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "timestamp", "successful", "ip_address")
    list_filter = ("successful", "timestamp")
    search_fields = ("user__email", "ip_address")

admin.site.register(LoginAttempt, LoginAttemptAdmin)
