from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date_format(date):
    date_str = date.strftime("%Y-%m-%d")
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Date format must be YYYY-MM-DD")


def validate_more_than_one_word(value):
    words = value.split()
    if len(words) <= 1:
        raise ValidationError("This field must have more than two words")


def validate_value_is_empty(value):
    if value is None or (isinstance(value, str) and len(value.strip()) <= 0):
        raise ValidationError("This field cannot be empty")
