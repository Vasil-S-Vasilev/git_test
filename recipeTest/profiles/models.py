from django.db import models
from profiles.validators import NicknameLengthValidator
from django.core.validators import MinLengthValidator, RegexValidator

# Create your models here.

class Profile(models.Model):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        blank=False,
        null=False,
        validators=[
            NicknameLengthValidator(),
        ]
    )

    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^[A-Z][a-zA-Z]*$",
                message="Name must start with a capital letter!"
            )
        ]
    )

    last_name = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^[A-Z][a-zA-Z]*$",
                message="Name must start with a capital letter!"
            )
        ]
    )

    chef = models.BooleanField(
        default=False,
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )



    