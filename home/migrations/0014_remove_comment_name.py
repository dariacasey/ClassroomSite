# Generated by Django 4.2.5 on 2023-10-27 03:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0013_comment_author"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="name",
        ),
    ]