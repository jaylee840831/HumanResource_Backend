# Generated by Django 5.1.1 on 2024-11-19 09:43

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_user_id_user_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='experience',
            field=models.CharField(blank=True, max_length=4000),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=None),
        ),
    ]