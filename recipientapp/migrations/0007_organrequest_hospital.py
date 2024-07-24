# Generated by Django 5.0.5 on 2024-05-11 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hospitalapp", "0001_initial"),
        ("recipientapp", "0006_organtransactiondetail_hospital"),
    ]

    operations = [
        migrations.AddField(
            model_name="organrequest",
            name="hospital",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="organ_requests",
                to="hospitalapp.hospital",
                verbose_name="Hospital",
            ),
        ),
    ]