# Generated by Django 3.2.7 on 2021-09-20 03:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('device_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('humidity', 'humidity'), ('temperature', 'temperature')], max_length=30)),
                ('json_data', models.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sensors.device')),
            ],
        ),
    ]