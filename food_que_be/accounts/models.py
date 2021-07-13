from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
import uuid


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+6599999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=14, blank=True)
    is_user = models.BooleanField("user status",default=True)
    is_tasker = models.BooleanField("tasker status",default=False)

    