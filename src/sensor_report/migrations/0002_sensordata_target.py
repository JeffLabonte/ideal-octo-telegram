# Generated by Django 3.2.8 on 2021-10-16 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_target', '0001_initial'),
        ('sensor_report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sensor_target.sensortarget'),
        ),
    ]