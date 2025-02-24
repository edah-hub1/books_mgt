from rest_framework import serializers
from .models import Book
from datetime import date
import re


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"  # Include all fields

    def validate_isbn(self, value):
        """Ensure the ISBN is either 10 or 13 digits long."""
        if not re.fullmatch(r"\d{10}|\d{13}", value):
            raise serializers.ValidationError("ISBN must be exactly 10 or 13 digits.")
        return value

    def validate_publication_date(self, value):
        """Ensure the publication date is not in the future."""
        if value > date.today():
            raise serializers.ValidationError(
                "Publication date cannot be in the future."
            )
        return value
