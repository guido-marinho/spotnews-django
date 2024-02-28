from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from news.validators import (
    validate_date_format,
    validate_more_than_one_word,
    validate_value_is_empty,
)


class Category(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
    )

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
    )
    email = models.EmailField(
        max_length=200,
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
    )
    password = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
    )
    role = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
    )

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[
            validate_value_is_empty,
            validate_more_than_one_word,
            MaxLengthValidator(200),
        ],
    )
    content = models.TextField(
        validators=[validate_value_is_empty],
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users"
    )
    created_at = models.DateField(
        validators=[validate_value_is_empty, validate_date_format],
    )
    image = models.ImageField(null=True, blank=True, upload_to="img/")
    categories = models.ManyToManyField(
        Category,
        validators=[validate_value_is_empty],
    )

    def __str__(self):
        return self.title
