# Generated by Django 5.1.1 on 2024-11-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_profile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]