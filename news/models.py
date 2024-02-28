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
    email = models.EmailField()
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
            MinLengthValidator(1),
            MaxLengthValidator(200),
            validate_more_than_one_word,
            validate_value_is_empty,
        ],
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(1),
            validate_value_is_empty,
        ],
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True,
        validators=[validate_date_format, validate_value_is_empty],
    )
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    categories = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
