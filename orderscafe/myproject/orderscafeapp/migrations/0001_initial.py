# Generated by Django 5.1.7 on 2025-03-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                (
                    "cdate",
                    models.DateTimeField(auto_now_add=True, verbose_name="created data"),
                ),
                (
                    "mdate",
                    models.DateTimeField(auto_now=True, verbose_name="modified data"),
                ),
                ("name", models.CharField(max_length=255, verbose_name="dish name")),
                (
                    "price",
                    models.DecimalField(decimal_places=2, max_digits=10, verbose_name="price"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Orders",
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
                (
                    "cdate",
                    models.DateTimeField(auto_now_add=True, verbose_name="created data"),
                ),
                (
                    "mdate",
                    models.DateTimeField(auto_now=True, verbose_name="modified data"),
                ),
                ("table_number", models.IntegerField(verbose_name="table number")),
                (
                    "total_price",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=10,
                        null=True,
                        verbose_name="total price",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("w", "wait"), ("r", "ready"), ("p", "paid")],
                        default="w",
                        max_length=2,
                        verbose_name="status",
                    ),
                ),
                (
                    "items",
                    models.ManyToManyField(
                        related_name="order_items",
                        to="orderscafeapp.dish",
                        verbose_name="items",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
