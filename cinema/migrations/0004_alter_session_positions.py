# Generated by Django 3.2.4 on 2022-10-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_session_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='positions',
            field=models.JSONField(default=''),
        ),
    ]
