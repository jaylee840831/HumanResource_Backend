# Generated by Django 5.1.1 on 2024-11-23 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_birth_date_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
