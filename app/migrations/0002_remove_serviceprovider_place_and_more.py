# Generated by Django 5.0.1 on 2024-02-13 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='place',
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.locations'),
        ),
    ]