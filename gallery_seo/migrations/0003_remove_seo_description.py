# Generated by Django 3.2.4 on 2022-10-05 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_seo', '0002_seo_description_seo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seo',
            name='description',
        ),
    ]
