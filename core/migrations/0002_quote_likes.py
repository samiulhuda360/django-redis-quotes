# Generated by Django 5.2 on 2025-04-18 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
