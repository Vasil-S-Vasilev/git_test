from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re


@deconstructible
class NicknameLengthValidator:
    def __init__(self, message=None):
        self.message = message or "Nickname must be at least 2 chars long!"

    def __call__(self, value, *args, **kwds):
        if len(value) < 2:
            raise ValidationError(self.message)
        
