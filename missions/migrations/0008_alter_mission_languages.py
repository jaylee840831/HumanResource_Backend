# Generated by Django 5.1.1 on 2024-12-06 11:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0007_alter_mission_languages_alter_mission_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None),
        ),
    ]
