# Generated by Django 5.1.1 on 2024-12-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
