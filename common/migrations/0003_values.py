# Generated by Django 5.1.1 on 2024-12-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_languages_language_tw_skills_skill_tw'),
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('value_tw', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
