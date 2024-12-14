# Generated by Django 5.1.4 on 2024-12-14 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Collabrium", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Podkast",
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
                ("total", models.CharField(max_length=200, verbose_name="инструмент")),
                ("image", models.ImageField(upload_to="", verbose_name="изображение")),
            ],
        ),
    ]