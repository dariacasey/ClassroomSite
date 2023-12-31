# Generated by Django 4.2.5 on 2023-10-24 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lessons", "0021_remove_lesson_lesson_class_lesson_lesson_class"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExerciseAttempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("attempt_number", models.PositiveIntegerField(default=1)),
                (
                    "selected_option",
                    models.PositiveIntegerField(
                        choices=[(1, "Option 1"), (2, "Option 2"), (3, "Option 3")]
                    ),
                ),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lessons.exercise",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
