from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
from recipes.choices import CuisineChoices
# Create your models here.


class Recipe(models.Model):

    title = models.CharField(
        unique=True,
        max_length=100,
        validators=[
            MinLengthValidator(10),
        ],
        error_messages={
            'unique': "We already have a recipe with the same title!"
        }
    )

    cuisine_type = models.CharField(
        max_length=7,
        choices=CuisineChoices.choices,
    )

    ingredients = models.TextField(
        help_text="Ingredients must be separated by a comma and space."
    )

    instructions = models.TextField()

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        help_text= "Provide the cooking time in minutes."
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    author = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='recipes',
    )

