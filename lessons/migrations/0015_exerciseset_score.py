# Generated by Django 4.2.5 on 2023-09-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0014_exerciseset"),
    ]

    operations = [
        migrations.AddField(
            model_name="exerciseset",
            name="score",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
