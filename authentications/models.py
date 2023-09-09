from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        "username",
        max_length=150,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(null=True, blank=True)
    is_vendor = models.BooleanField(default=False,null=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
