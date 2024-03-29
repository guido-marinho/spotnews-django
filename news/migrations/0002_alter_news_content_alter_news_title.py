# Generated by Django 4.2.3 on 2024-02-28 16:29

import django.core.validators
from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(
                validators=[
                    news.validators.validate_more_than_one_word,
                    news.validators.validate_value_is_empty,
                ]
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[
                    django.core.validators.MaxLengthValidator(200),
                    news.validators.validate_more_than_one_word,
                    news.validators.validate_value_is_empty,
                ],
            ),
        ),
    ]
