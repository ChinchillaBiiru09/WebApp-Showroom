# Generated by Django 5.2 on 2025-04-23 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
    ]
