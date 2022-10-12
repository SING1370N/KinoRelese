# Generated by Django 4.0.7 on 2022-08-20 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_ticket_buyer_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Gallery'},
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='gallery_id',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.PROTECT, to='main.gallery'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
