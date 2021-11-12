# Generated by Django 3.2.9 on 2021-11-12 03:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sensor", "0002_alter_sensor_name"),
        ("sensor_target", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SensorTarget",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(
                        choices=[("str", "String"), ("int", "Integer"), ("float", "Float"), ("bool", "Boolean")],
                        max_length=5,
                    ),
                ),
                ("value", models.CharField(max_length=20)),
                ("sensor", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="sensor.sensor")),
                (
                    "target",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="sensor_target.sensortarget"
                    ),
                ),
            ],
        ),
    ]
