from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# create a new user

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    # create a superuser
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_img.png"}'


def get_default_profile_image():
    return "/profile_img.png"


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_img = models.ImageField(max_length=255, upload_to=get_profile_image_filepath, null=True, blank=True,
                                    default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()  # tie the account to custom account manager

    USERNAME_FIELD = 'email'  # to enable logging with email instead of username
    REQUIRED_FIELDS = ['username']

    # override this three functions:
    # define what is going to be returned if object is accessed without any of the individual fields
    def __str__(self):
        return self.username

    # set default permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_profile_image_name(self):
        return str(self.profile_img)[str(self.profile_img).index(f'profile_images/{self.pk}/'):]
