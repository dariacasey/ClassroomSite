# Generated by Django 4.2.5 on 2023-09-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("classes", "0002_alter_class_class_code"),
        ("lessons", "0020_lesson_lesson_class"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="lesson_class",
        ),
        migrations.AddField(
            model_name="lesson",
            name="lesson_class",
            field=models.ManyToManyField(related_name="lessons", to="classes.class"),
        ),
    ]
