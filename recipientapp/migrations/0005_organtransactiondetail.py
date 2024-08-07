# Generated by Django 5.0.5 on 2024-05-11 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipientapp", "0004_alter_organrequest_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganTransactionDetail",
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
                ("transaction_hash", models.CharField(max_length=64)),
                ("sender_address", models.CharField(max_length=42)),
                ("contract_address", models.CharField(max_length=42)),
                ("gas_used", models.BigIntegerField()),
                ("block_number", models.BigIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "organ_request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organ_transaction_details",
                        to="recipientapp.organrequest",
                    ),
                ),
            ],
        ),
    ]
