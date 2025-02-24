from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
import re


def validate_isbn(value):
    """Ensure the ISBN is either 10 or 13 digits long."""
    if not re.fullmatch(r"\d{10}|\d{13}", value):
        raise ValidationError("ISBN must be exactly 10 or 13 digits.")


def validate_publication_date(value):
    """Ensure the publication date is not in the future."""
    if value > date.today():
        raise ValidationError("Publication date cannot be in the future.")


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(validators=[validate_publication_date])
    isbn = models.CharField(max_length=13, unique=True, validators=[validate_isbn])
    summary = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
