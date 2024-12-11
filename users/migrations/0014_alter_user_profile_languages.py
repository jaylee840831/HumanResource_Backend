# Generated by Django 5.1.1 on 2024-12-06 11:36

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_user_profile_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), blank=True, size=None),
        ),
    ]
