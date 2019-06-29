from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    """
    User
        This class define model used to store user entity details.
            Inherits : `BaseModelMixin`, `AbstractBaseUser`
            properties : permissions
    """
    mobile_number = models.CharField(
        unique=True,
        max_length=15,
        verbose_name='Mobile Number',
        db_index=True,
    )
    email = models.EmailField(verbose_name='Email Address')
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # def invalidate_user_jwt_token(self):
    #     """
    #     invalidate_user_jwt_token
    #         A utility to invalidate user token
    #     :return:
    #     """
    #     self.jwt_secret = core_models.string_uuid()
    #     self.save()

    def __str__(self):
        return self.mobile_number