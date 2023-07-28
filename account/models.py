from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager, AbstractUser


class CustomBaseUserManager(BaseUserManager):
    """
    creating custom baseuser manager that will use email
    as authentication instead of inbuilt username
    """

    def create_user(
            self, email: str, password: str, **extra_fields: str
            ) -> str:
        """
        this function is use to create a new regular user
        """
        if not email:
            raise ValueError(_("email address must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
            self, email: str, password: str, **extra_fields: str
            ) -> str:
        """
        this function is use to create a new superuser or staff
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("superuser must have is_staff set to True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("superuser must have is_superuser set to True"))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    custom user class to overide the inbuilt user
    so extra fields can be add to the user model
    """
    username = None
    email = models.EmailField(_("email address"), unique=True)
    confirm_email_token = models.CharField(_("confirm email token"),
                                           max_length=100)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomBaseUserManager()

    def __str__(self) -> str:
        return self.email
