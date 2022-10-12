# Generated by Django 4.0.7 on 2022-08-20 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_gallery_options_remove_gallery_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.gallery'),
        ),
        migrations.AddField(
            model_name='contact',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.gallery'),
        ),
        migrations.AddField(
            model_name='film',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.gallery'),
        ),
        migrations.AddField(
            model_name='room',
            name='gallery',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.gallery'),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='banner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='banner', to='main.image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.gallery'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='room',
            name='banner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.image'),
        ),
    ]