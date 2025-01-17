# Generated by Django 5.1 on 2024-12-29 00:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Stores",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("custom_identifier", models.CharField(max_length=255)),
                ("shipping_tax_status", models.BooleanField(blank=True, default=False, null=True)),
                ("url", models.CharField(blank=True, max_length=255, null=True)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("logo", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="StoreTypes",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        choices=[("salla", "Salla"), ("zid", "Zid"), ("shopify", "Shopify")], max_length=255
                    ),
                ),
                ("logo", models.URLField(blank=True, null=True)),
                ("url", models.URLField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name_ar", models.CharField(max_length=255)),
                ("name_en", models.CharField(max_length=255)),
                ("sku", models.CharField(max_length=255)),
                ("description", models.JSONField(blank=True, null=True)),
                ("price", models.BigIntegerField(blank=True, null=True)),
                ("quantity", models.PositiveBigIntegerField()),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="products", to="stores.stores"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="stores",
            name="store_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="stores", to="stores.storetypes"
            ),
        ),
        migrations.CreateModel(
            name="Customers",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("store_type_identifier", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("mobile", models.CharField(blank=True, max_length=15, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True, choices=[("male", "male"), ("female", "female")], max_length=45, null=True
                    ),
                ),
                ("stores", models.ManyToManyField(blank=True, related_name="customers", to="stores.stores")),
                (
                    "store_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="customers", to="stores.storetypes"
                    ),
                ),
            ],
            options={
                "unique_together": {("store_type", "store_type_identifier")},
            },
        ),
        migrations.CreateModel(
            name="Orders",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("order_id", models.TextField()),
                ("order_id_extra", models.TextField(blank=True, null=True)),
                ("order_date", models.DateTimeField()),
                ("total_price", models.FloatField()),
                ("exchange_rate_to_sar", models.FloatField(default=1.0)),
                ("currency", models.CharField(default="SAR", max_length=255)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="orders", to="stores.customers"
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="orders", to="stores.stores"
                    ),
                ),
            ],
            options={
                "unique_together": {("order_id", "store")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="stores",
            unique_together={("custom_identifier", "store_type")},
        ),
    ]
