# Generated by Django 5.1.1 on 2024-12-06 18:03

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0008_alter_mission_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, size=None),
        ),
        migrations.AlterField(
            model_name='mission',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, size=None),
        ),
    ]
