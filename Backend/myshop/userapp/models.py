from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, _("Admin")
        STAFF = 2, _("Staff")
        USER = 3, _("User")

    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=RoleChoices.choices, default=RoleChoices.USER)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    otp_secret = models.CharField(max_length=64, blank=True, null=True)  # For OTP verification
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class LoginAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_attempts')
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    is_active = models.BooleanField(default=False)  # Track active login sessions
    device_details = models.CharField(max_length=255, blank=True, null=True)  # Track device details

    def __str__(self):
        return f"{self.user.email} - {'Success' if self.successful else 'Failed'} at {self.timestamp}"
