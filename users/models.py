from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from event_app.models import Organization
from .managers import CustomUserManager
from django.db import models
import os
from django.conf import settings
from django.template.defaultfilters import slugify


# модель пользователя
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    object = CustomUserManager()

    def __str__(self):
        return self.email


# модель профиля пользователя
def get_image_filename(instance, filename):
    name = instance.product.name
    slug = slugify(name)
    return f"products/{slug}-{filename}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_image_filename, blank=True)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def filename(self):
        return os.path.basename(self.image.name)
