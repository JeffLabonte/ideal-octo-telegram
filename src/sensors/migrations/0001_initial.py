# Generated by Django 3.2.7 on 2021-10-05 01:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("device_name", models.CharField(max_length=60, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sensors",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(choices=[("humidity", "humidity"), ("temperature", "temperature")], max_length=30),
                ),
                ("json_data", models.JSONField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "device",
                    models.ForeignKey(
                        default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to="sensors.device"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="IpAddress",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ("ip_address", models.CharField(max_length=15)),
                ("device", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensors.device")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
