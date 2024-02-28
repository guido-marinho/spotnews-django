# Generated by Django 4.2.3 on 2024-02-28 18:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="news.user",
            ),
        ),
        migrations.RemoveField(
            model_name="news",
            name="categories",
        ),
        migrations.AlterField(
            model_name="news",
            name="content",
            field=models.TextField(
                validators=[news.validators.validate_value_is_empty]
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="created_at",
            field=models.DateField(
                validators=[
                    news.validators.validate_value_is_empty,
                    news.validators.validate_date_format,
                ]
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="title",
            field=models.CharField(
                max_length=200,
                validators=[
                    news.validators.validate_value_is_empty,
                    news.validators.validate_more_than_one_word,
                    django.core.validators.MaxLengthValidator(200),
                ],
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="categories",
            field=models.ManyToManyField(
                to="news.category",
                validators=[news.validators.validate_value_is_empty],
            ),
        ),
    ]
